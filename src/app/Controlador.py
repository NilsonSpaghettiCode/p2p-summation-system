'''
Clase Controlador
-----------------
Esta clase contiene toda la logica de la aplicacion, utilizando los 
metodos publicados por las otras clases para realizar todos los procedimientos
'''
from .Nodo import Nodo


class Controlador:
    '''
    La clase Controlador permite conectar las clases con los datos introducidos
    por el usuario
    '''
    def __init__(self):
        '''
        Constructor de la clase Controlador
        '''
        pass

    def insertar_numero(self, nodo:Nodo, numero):
        '''
        Este metodo utiliza los metodos de nodo para insertar los numeros en la lista 
        del nodo y establece la respuesta de la transaccion

        :param nodo: El nodo al que se le va añadir el numero
        :type nodo: Nodo<Object>
        :param numero: el numero que sera insertado
        :type numero: str
        :returns: la respuesta de la insercion del numero
        :rtype: dict
        '''
        try:
            nodo.insertar_numero(int(numero))
            return self.establecer_respuesta(True, contenido=[numero])
        except Exception as e:
            return self.establecer_respuesta(contenido=[numero]) 
    
    def establecer_respuesta(self, estado=False,contenido=[]):
        '''
        Este metodo establece la respuesta que sera enviada

        :param estado: El estado de la respuesta
        :type estado: bool
        :returns: la respuesta a manera de diccionario con su estado y contenido
        :rtype: dict
        '''
        respuesta_formato = {
            'estado':estado,
            'contenido':contenido
        }
        return respuesta_formato
    
    def obtener_suma(self, nodo:Nodo, lista_vecinos_confirmados=[], origen="192.168.0.1:4900"):
        '''
        Este metodo permite obtener la suma total de la red

        :param nodo: El nodo al que se le obtendra la suma
        :type nodo: Nodo<Object>
        :param lista_vecinos_confirmados: La lista de nodos que ya han realizado una peticion
        :type lista_vecinos_confirmados: list
        :param origen: El origen de la peticion
        :type origen: str
        :returns: la respuesta de la suma de los nodos
        :rtype: dict
        '''
        suma_nodo_actual = nodo.obtener_suma_red(lista_vecinos_confirmados, origen)
        '''
        suma_vecinos_nodo_actual = nodo
        '''
        respuesta = {'suma_total': suma_nodo_actual}
        
        return respuesta
    
    def validar_solicitud(self, identificador_solicitud:str, nodo:Nodo):
        '''
        Este metodo valida el identificador de la solicitud para conocer si la peticion ya ha sido
        realizada, y sino procede a realizarla añadiendo el identificador a la lista de solicitudes

        :param identificador_solicitud: id obtenido de request
        :type identificador_solicitud: str
        :param nodo: Nodo representativo en al red
        :type nodo: Nodo
        '''
        peticion_encontrada = nodo.buscar_peticion(identificador_solicitud)
        if not peticion_encontrada:
            nodo.master_actual = identificador_solicitud
        
        return peticion_encontrada            
        