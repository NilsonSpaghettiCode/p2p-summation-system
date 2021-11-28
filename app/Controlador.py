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
        if(self.es_numero(numero)):
            nodo.insertar_numero(numero)
            return self.establecer_respuesta(True, contenido=[numero])
        return self.establecer_respuesta(contenido=[numero]) 
    
    def establecer_respuesta(self,estado=False,contenido=[]):
        respuesta_formato = {
            'estado':estado,
            'contenido':contenido
        }
        return respuesta_formato
        

    def es_numero(self, numero):

        if type(numero) == int:
            return True
            
        return False