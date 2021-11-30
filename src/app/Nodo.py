'''
Clase Nodo
----------
Este modulo contiene toda la informacion requerida para cada nodo
del sistema de iguales a iguales (peer to peer)
'''
from .HttpSolicitud import HttpSolicitud 
from ..config import funciones_config

class Nodo:
    '''
    La clase nodo, es el objeto que describe la informacion
    del nodo especifico y guarda los datos necesarios para
    realizar la suma
    '''
    
    def __init__(self, direccion_ip:str='0.0.0.0', nombre:str = 'nodo-default', identificador_hash:str ='', lista_numeros:list = [50,70], lista_nodos_vecinos:list = [], estado:int=0, puerto:int = 5200):
        '''
        Constructor de la clase nodo

        :param direccion_ip: la dirección ip del nodo
        :type direccion_ip: str
        :param nombre: el nombre del nodo
        :type nombre: str
        :param identificador_hash: identificador del nodo con una función hash 
        :type identificador_hash: str
        :param lista_numeros: la lista de numeros del nodo
        :type lista_numeros: list
        :param lista_nodos_vecinos: la lista de nodos que hacen de vecinos del nodo instanciado en la aplicación
        :type lista_nodos_vecinos: list
        '''
        self.nombre = nombre
        self.direccion_ip = direccion_ip
        self.identificador_hash = identificador_hash
        self.lista_numeros = lista_numeros 
        self.lista_nodos_vecinos = lista_nodos_vecinos
        self.estado=1
        self.puerto = puerto
        self.peticiones_con_respuesta = []
        self.master_actual = ""
    
    def __str__(self):
        '''
        Funcion para describir el objeto a manera de cadena
            
        :returns: objeto en cadena
        :rtype: str
        '''
        nodo_cadena = f'''Identificador nodo: {self.identificador_hash},\nNombre: {self.nombre},\nDireccion ip: {self.direccion_ip},\nLista numeros: {self.lista_numeros},\nNodos vecinos: {self.lista_nodos_vecinos}'''

        return nodo_cadena

    def insertar_numero(self, numero:int):
        '''
        Este metodo inserta el numero digitado por el usuario 
        en la lista de numeros

        :param numero: Numero el cual va a ingresar en el nodo actual
        :type numero: int
        :returns: el estado del ingreso del numero, si es valido, ademas del propio numero
        :rtype: dict
        '''    
        self.lista_numeros.append(numero)
        return {'estado':True, 'numero':numero}
    
    def obtener_suma_nodal(self):
        '''
        Este metodo permite obtener la suma de los numeros en el nodo

        :returns: retorna la suma de numero de la lista del nodo actual
        :rtype: int
        '''
        suma:int = 0
        
        for numero in self.lista_numeros:
            suma  += numero 

        return suma

    def obtener_suma_red(self, lista_vecinos_confirmados, origen):
        
        suma_nodo_actual = self.obtener_suma_nodal()
        suma_total_vecinos = 0
        if self.lista_nodos_vecinos: #Si no esta vacia (si sí tiene vecinos)
            lista_auxiliar = self.filtrar_nodos_solicitados(lista_vecinos_confirmados, origen)
            print("Lista auxiliar:", lista_auxiliar)
            suma_total_vecinos = self.pedir_suma_vecinos(lista_auxiliar)
            
        suma_total = suma_nodo_actual + suma_total_vecinos
        '''
        respuesta = {
            'nodos_sumados':[ # {'direccion_ip': '', 'nombre': '', 'suma_nodo' = 0}

            ],
            'suma_total':0
        }
        suma_nodo_actual = self.obtener_suma_nodal()

        nodo_vecinos = self.obtener_suma_vecinos(lista_vecinos_confirmados)

        respuesta['suma_total'] += suma_nodo_actual
        print("AQUI", nodo_vecinos)
        for nodo in nodo_vecinos:
            respuesta['suma_total'] += nodo['suma_nodo']
        '''         
        return suma_total
    
    def pedir_suma_vecinos(self, lista_nodos_aux):
        suma_total_vecinos = 0
        for vecinos in lista_nodos_aux:
            ip_v = vecinos['ip']
            puerto_v = vecinos['puerto']
            formato_solicitud = HttpSolicitud.establecer_formato_diccionario(lista_nodos_aux,self.direccion_ip,self.puerto, self.calcular_identificador_de_solicitud())
            print('FORMATO', formato_solicitud)
            solicitud_servicio = HttpSolicitud.consumir_servicio(ip_v, puerto_v,datos_solicitud=formato_solicitud)
            suma_total_vecinos += int(solicitud_servicio['suma_total']) #implementar como actuar si estado solicitud es falso
        return suma_total_vecinos
             
    def filtrar_nodos_solicitados(self, lista_vecinos_confirmados:list, origen):
        '''
        '''
        lista_auxiliar = [] 
        for vecino_del_nodo_actual in self.lista_nodos_vecinos: #1 [1,2,3,4] 
            direccion_ip_nodo_actual = f'{vecino_del_nodo_actual["ip"]}:{vecino_del_nodo_actual["puerto"]}'
            print(self.lista_nodos_vecinos)

            if not direccion_ip_nodo_actual == origen: # 3
                
                nodo_esta_repetido = False
                for vecinos_nodo_peticion in lista_vecinos_confirmados: #[2,4,1]
                    print(lista_vecinos_confirmados)
                    
                    print(vecinos_nodo_peticion)
                    direccion_ip_nodo_perticionario = f'{vecinos_nodo_peticion["ip"]}:{vecinos_nodo_peticion["puerto"]}'
                    
                    if direccion_ip_nodo_actual == direccion_ip_nodo_perticionario or direccion_ip_nodo_perticionario == self.direccion_ip:
                        nodo_esta_repetido = True
                        break

                    #nodo_vecinod_apuntador = vecinos_nodo_peticion
 

                if not nodo_esta_repetido:
                    lista_auxiliar.append(vecino_del_nodo_actual)

        return lista_auxiliar

    def es_nodo_confirmado(self, lista_vecinos_confirmados:list, ip_vecino_actual:dict):
        '''
        Esta funcion comprueba la existencia del nodo en la lista de los confirmados

        :param lista_vecinos_confirmados: los vecinos confirmados
        :type lista_vecinos_confirmados: list
        :param ip_vecino_actual: la direccion del vecino a comprobar
        :type ip_vecino_actual: str
        :returns: retorna un boolean si encuentra una confirmacion
        :rtype: bool
        '''
        confirmacion = False

        for vecino_confirmado in lista_vecinos_confirmados:
            if vecino_confirmado['ip'] == ip_vecino_actual:
                confirmacion = True
                break
        
        return confirmacion

    def cargar_nodos_vecinos(self, nodos_vecinos:list):
        '''
        Este metodo permite establecer los nodos vecinos de un nodo por medio de la lista
        
        :param nodos_vecinos: lista de nodos vecinos para establecer
        :type nodos_vecinos: list
        '''
            
        self.lista_nodos_vecinos = nodos_vecinos
    
    
    def calcular_identificador_de_solicitud(self):
        '''
        Este método crea el identificador de las solicitudes para
        definir un master    
        '''
        tiempo = funciones_config.obtener_tiempo()
        identificador = funciones_config.generar_hash_solicitud(self.nombre, self.direccion_ip, tiempo)

        return identificador

    
    def agregar_solicitud_con_respuesta(self, identificador_solicitud:str):
        '''
        Agrega el identificador de una solicitud a la cual se le dio respuesta

        :param identificador_solicitud: Identificador de una solicitud con respuesta
        :type identificador_solicitud: str
        :returns: None
        :rtype: None
        '''
        if not identificador_solicitud == '':
            self.peticiones_con_respuesta.append(identificador_solicitud)
        
    def buscar_peticion(self, identificador:str = ''):
        '''
        Este metodo busca la peticion que llega por un nodo en la lista de peticiones

        :param identificador_solicitud: Identificador obtenido de la request
        :type identificador_solicitud:
        '''
        
        peticion_en_lista = False

        for peticion in self.peticiones_con_respuesta:
            if peticion == identificador:
                peticion_en_lista = True 
                break
        
        return peticion_en_lista