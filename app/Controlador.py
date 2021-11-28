'''
Clase Controlador
-----------------
Esta clase contiene toda la logica de la aplicacion, utilizando los 
metodos publicados por las otras clases para realizar todos los procedimientos
'''
from app.Nodo import Nodo


class Controlador:
    def __init__(self):
        pass

    def insertar_numero(self, nodo:Nodo, numero):
        try:
            nodo.insertar_numero(int(numero))
            return self.establecer_respuesta(True, contenido=[numero])
        except Exception as e:
            return self.establecer_respuesta(contenido=[numero]) 
    
    def establecer_respuesta(self,estado=False,contenido=[]):
        respuesta_formato = {
            'estado':estado,
            'contenido':contenido
        }
        return respuesta_formato
        