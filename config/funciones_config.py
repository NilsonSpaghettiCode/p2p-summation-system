'''
Archivo funciones_config
------------------------
Este modulo contiene las funciones utilizadas por la configuración del nodo
'''

import hashlib
from pickle import dumps

def generar_hash_nodo(nombre:str='nodo-default', direccion:str='0.0.0.0'):
    '''
    Esta función genera un hash con la función SHA256 en base al 
    nombre y dirección del nodo

    :param nombre: el nombre del nodo en cuestion
    :type nombre: str
    :param direccion: la direccion ip del nodo
    :type direccion: str
    :returns: el hash generado del nodo
    :rtype: str
    '''
    contenido_hash = f'Nombre||{nombre}||Direccion||{direccion}'
    funcion_hash = hashlib.sha256(dumps(contenido_hash))
    hash_generado = funcion_hash.hexdigest()

    return hash_generado
