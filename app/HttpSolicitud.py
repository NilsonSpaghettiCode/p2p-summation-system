'''
Clase HttpSolicitud
-------------------
Esta clase contiene los metodos principales para consumir
los servicios de los demas nodos
'''

import requests
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

    def establecer_formato_diccionario(self, lista_peticiones:list):
        data = {
            'peticiones_realizadas':lista_peticiones, #[{'nombre': 'Nodo A', 'direccion': '127.0.0.1'}]
            }

        return data

    def consumir_servicio(self, direccion_ip:str = '0.0.0.0', puerto:int=0, datos_solicitud:dict = {}):
        '''
        Este metodo permite consumir un servicio publicado por otra aplicacion

        :param direccion_ip: la direccion ip del servicio que se desa consumir
        :type direccion_ip: str
        :param puerto: el puerto donde se aloja el servicio
        :type puerto: int
        :returns: los datos recibidos a manera de json
        :rtype: json
        '''
        uri=f'{direccion_ip}:{puerto}'
        respuestaJSON = {}
        try:
            datos_respuesta = requests.request(method='POST', url=uri, headers={},data=datos_solicitud)
            respuestaJSON = datos_respuesta.json()
        except Exception as error:
            print(error)
        
        return respuestaJSON