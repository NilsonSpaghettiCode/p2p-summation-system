'''
Clase HttpSolicitud
-------------------
Esta clase contiene los metodos principales para consumir
los servicios de los demas nodos
'''

import requests
import json
class HttpSolicitud:
    '''
    La clase HttpSolicitud contiene los metodos necesarios para
    comunicar a los nodos
    '''
    def __init__(self):
        '''
        Constructor de la clase HttpSolicitud
        '''
        pass
    @staticmethod
    def establecer_formato_diccionario(lista_nodos_solicitados:list = [], origen:str='0.0.0.0', puerto:int = 5200, identificador_solicitud:str = ''):
        '''
        Esta función le establece un formato a las peticiones realizadas al nodo

        :param lista_nodos_solicitados: las peticiones realizadas al nodo
        :type lista_nodos_solicitados: list
        :param origen: la direccion de donde proviene
        :type origen: str
        :returns: retorna las peticiones realizadas teniendo en cuenta el origen
        :rtype: dict
        '''
        
        data = {
            'nodos_sumados':lista_nodos_solicitados, #[{'nombre': 'Nodo A', 'direccion': '127.0.0.1'}]
            'origen_peticion': f'{origen}:{puerto}',
            'identificador_solicitud': identificador_solicitud
            }

        return json.dumps(data)
    @staticmethod
    def consumir_servicio(direccion_ip:str = 'localhost', puerto:int=5200, datos_solicitud:dict = {}):
        '''
        Este metodo permite consumir un servicio publicado por otra aplicacion

        :param direccion_ip: la direccion ip del servicio que se desa consumir
        :type direccion_ip: str
        :param puerto: el puerto donde se aloja el servicio
        :type puerto: int
        :returns: los datos recibidos a manera de json
        :rtype: json
        '''
        uri=f'http://{direccion_ip}:{puerto}/suma_de_red'
        #print(uri)
        respuestaJSON = {}
        try:
            datos_respuesta = requests.request(method='POST', url=uri, headers={'Content-Type': 'application/json'},data=datos_solicitud)
            respuestaJSON = datos_respuesta.json()
        except Exception as error:
            print("ERROR: ",error)
        
        return respuestaJSON