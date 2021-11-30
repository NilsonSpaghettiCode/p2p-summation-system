'''
Archivo main
------------
Este archivo contiene el inicio de la aplicacion nodo
'''
from src.app.service_main import start as run
from src.config.config import config_nodos, config_numero
from src.config.funciones_config import generar_hash_nodo

def main():
    '''
    Funcion main que ejecuta todo el funcionamiento del todo
    cargando primero el archivo de configuracion y estableciendo
    los valores iniciales del nodo
    '''
    cfg = config_nodos[config_numero]
    ip= cfg['ip_address']
    port = cfg['port']
    nodos_conocidos = cfg['nodos_conocidos']
    nombre_nodo = cfg['nombre_nodo']
    nuget = cfg['debug']
    hash_nodo = generar_hash_nodo(nombre_nodo, ip)
    
    run(ip, port, nodos_conocidos, nombre_nodo, hash_nodo, nuget)


if __name__ == '__main__':
    main()