
from flask import Flask, request
from flask.json import jsonify
from werkzeug.exceptions import BadRequestKeyError
from .Nodo import Nodo
from .Controlador import Controlador
app = Flask(__name__)
nodo = Nodo()
controlador = Controlador()

# <--------------------------- Servicios publicados --------------------------->

@app.route('/')
def informacion_nodo():
    '''
    Implementar servicio
    '''
    return jsonify(nodo.__dict__)

@app.route('/suma_de_red', methods=['GET'])
def sumar_red():

    '''
    Implementar servicio
    '''
    pass

@app.route('/guardarnumero', methods=['POST'])
def anadir_numero():
    '''
    Implementar servicio
    //print(request)
    '''
    respuesta = {}
    try:
        numero = request.form['numero']
        respuesta = controlador.insertar_numero(nodo,numero)
    except BadRequestKeyError as e:
        respuesta = {'Error': True, 'TypeError':'Parametro numero necesario'}
    return jsonify(respuesta)

# <--------------------------- Funciones aplicacion --------------------------->

def establecer_nodo(lista_nodos_vecinos,  ip, nombre, nodo_hash):
    '''
    Esta funcion establece los parametros para iniciar el nodo

    :param name:
    :type name:
    :param name:
    :type name:
    :param name:
    :type name:
    :param name:
    :type name:
    '''
    nodo.lista_nodos_vecinos = lista_nodos_vecinos
    nodo.direccion_ip = ip
    nodo.nombre = nombre
    nodo.identificador_hash = nodo_hash

def start(ip:str, port:int, lista_nodos_vecinos:list, nombre, nodo_hash):
    '''
    Función de inicio de aplicación (nodo)
    
    :param ip: la dirección ip del nodo
    :type ip: str
    :param port: el puerto donde se aloja la aplicación (nodo)
    :type port: int
    :param lista_nodos_vecinos: la lista de los nodos que conoce la aplicación
    :type lista_nodos_vecinos: list
    '''
    establecer_nodo(lista_nodos_vecinos,  ip, nombre, nodo_hash)
    print('Running...')
    print('-'*100)
    print(nodo)
    print('-'*100)
    app.run(ip, port, debug=True)
   
