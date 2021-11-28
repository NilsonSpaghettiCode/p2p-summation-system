'''
Clase Nodo
----------
Este modulo contiene toda la informacion requerida para cada nodo
del sistema de iguales a iguales (peer to peer)
'''
class Nodo:
    '''
    La clase nodo, es el objeto que describe la informacion
    del nodo especifico y guarda los datos necesarios para
    realizar la suma
    '''
    
    
    def __init__(self, direccion_ip:str='0.0.0.0', nombre:str = 'nodo-default', identificador_hash:str ='', lista_numeros:list = [], lista_nodos_vecinos:list = [], estado:int=0):
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
        
    def cargar_nodos_vecinos(self, nodos_vecinos:list):
        '''
        Este metodo permite establecer los nodos vecinos de un nodo por medio de la lista
        
        :param nodos_vecinos: lista de nodos vecinos para establecer
        :type nodos_vecinos: list
        '''
            
        self.lista_nodos_vecinos = nodos_vecinos
    
    