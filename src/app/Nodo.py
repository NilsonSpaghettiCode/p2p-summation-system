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
    
    def __init__(self, direccion_ip:str='0.0.0.0', nombre:str = 'nodo-default', identificador_hash:str ='', lista_numeros:list = [], lista_nodos_vecinos:list = [], estado:int=0, puerto:int = 5200):
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
        self.es_master = False
        self.suma_nodo = 0
    
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

        self.suma_nodo = suma

        return suma

    def obtener_suma_red(self, lista_vecinos_confirmados, origen):
        '''
        Este metodo realiza toda la logica para obtener la suma de la red
        utilizando los atributos del nodo

        :param lista_vecinos_confirmados: la lista de vecinos que ya han recibido la solicitud
        :type lista_vecinos_confirmados: list
        :param origen: La direccion de donde provino la solicitud
        :type origen: str
        :returns: la suma de los nodos
        :rtype: dict
        '''
        
        suma_nodo_actual = self.obtener_suma_nodal()
        #lista_nodos_suma = [{self.nombre:self.obtener_suma_nodal()}]
        suma_total_vecinos = {}
        if self.lista_nodos_vecinos: #Si no esta vacia (si sí tiene vecinos)
            lista_auxiliar = self.filtrar_nodos_solicitados(lista_vecinos_confirmados, origen)
            #print("Lista auxiliar:", lista_auxiliar)
            suma_total_vecinos = self.pedir_suma_vecinos(lista_auxiliar, lista_vecinos_confirmados)

            
        suma_total = suma_nodo_actual + suma_total_vecinos['suma_total']
        nueva_lista_nodos_suma = []
        nueva_lista_nodos_suma.extend(suma_total_vecinos['nodos_suma'])
        nueva_lista_nodos_suma.append({self.nombre:suma_nodo_actual})
        respuesta = {'suma_total':suma_total,'nodos_suma':nueva_lista_nodos_suma}
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
        return respuesta
    
    def pedir_suma_vecinos(self, lista_nodos_aux, lista_vecinos_confirmados):
        '''
        Este metodo solicita la suma a los nodos vecinos

        :param lista_nodos_aux: la lista de nodos que ya han recibido una peticion por el nodo anterior
        :type lista_nodos_aux: list
        :param lista_vecinos_confirmados: la lista de vecinos que ya confirmaron la peticion
        :type lista_vecinos_confirmados: list
        :returns: la suma total de los vecinos del nodo
        :rtype: list
        '''
        suma_total_vecinos = 0
        lista_nodos_suma = []
        lista_sumada_con_filtro = []
        lista_sumada_con_filtro.extend(lista_nodos_aux)
        lista_sumada_con_filtro.extend(lista_vecinos_confirmados)
        #print("Lista a enviar a vecinos:", lista_sumada_con_filtro)
        formato_solicitud = self.obtener_formato_solicitud_suma(lista_sumada_con_filtro)
        #print("Formato generado:" , formato_solicitud)
        for vecinos in lista_nodos_aux:
            ip_v = vecinos['ip']
            puerto_v = vecinos['puerto']
            
            #print('FORMATO', formato_solicitud)

            solicitud_servicio = HttpSolicitud.consumir_servicio(ip_v, puerto_v,datos_solicitud=formato_solicitud)
            #print("Solicitud enviada a ->",ip_v)
            suma_total_vecinos += int(solicitud_servicio['suma_total']) #implementar como actuar si estado solicitud es falso
            lista_nodos_suma.extend(solicitud_servicio['nodos_suma']) 

        respuesta= {'suma_total':suma_total_vecinos,'nodos_suma':lista_nodos_suma}
        return respuesta

    def obtener_formato_solicitud_suma(self, lista_nodos_aux):
        '''
        Este metodo obtiene el formato de la suma de los nodos

        :param lista_nodos_aux: la lista de nodos que ya han recibido una peticion por el nodo anterior
        :type lista_nodos_aux: list
        :returns: el formato de la suma
        :rtype: dict
        '''
        formato_solicitud = {}
        if self.es_master:
            identificador_master = self.calcular_identificador_de_solicitud()
            formato_solicitud = HttpSolicitud.establecer_formato_diccionario(lista_nodos_aux,self.direccion_ip,self.puerto, identificador_master)
        else:
            formato_solicitud = HttpSolicitud.establecer_formato_diccionario(lista_nodos_aux,self.direccion_ip,self.puerto, self.master_actual)
        
        return formato_solicitud
                  
    def filtrar_nodos_solicitados(self, lista_vecinos_confirmados:list, origen):
        '''
        Este metodo permite filtrar los nodos que ya han sido solicitados

        :param lista_vecinos_confirmados: la lista de los vecinos que ya han sido confirmados
        :type lista_vecinos_confirmados: list
        :param origen: el origen de la peticion 
        :type origen: str
        :returns: la lista auxiliar con los nodos filtrados
        :rtype: list
        '''
        #print("Lista de llegada", lista_vecinos_confirmados)
        lista_auxiliar = [] 
        for vecino_del_nodo_actual in self.lista_nodos_vecinos: #1 [1,2,3,4] 
            direccion_ip_nodo_actual = f'{vecino_del_nodo_actual["ip"]}:{vecino_del_nodo_actual["puerto"]}'
            #print(self.lista_nodos_vecinos)

            if not direccion_ip_nodo_actual == origen: # 3
                
                nodo_esta_repetido = False
                for vecinos_nodo_peticion in lista_vecinos_confirmados: #[2,4,1]
                   #print(lista_vecinos_confirmados)
                    
                   #print(vecinos_nodo_peticion)
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

        :returns: el hash de la solicitud
        :rtype: str   
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
        :type identificador_solicitud: str
        :returns: un boolean si encuentra la solicitud
        :rtype: bool
        '''
        
        peticion_en_lista = False

        for peticion in self.peticiones_con_respuesta:
            if peticion == identificador:
                peticion_en_lista = True 
                break
        
        return peticion_en_lista