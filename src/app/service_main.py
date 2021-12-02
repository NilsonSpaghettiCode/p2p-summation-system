'''
Servicios Nodo
--------------
Este modulo contiene los servicios que publica el nodo
para el funcionamiento de la aplicacion
'''

from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

from werkzeug.exceptions import BadRequestKeyError
from .Nodo import Nodo
from .Controlador import Controlador
app = Flask(__name__)
cors = CORS(app)

nodo = Nodo()
controlador = Controlador()

app.config['CORS_HEADER'] = 'Content-Type'

# <--------------------------- Servicios publicados --------------------------->

@cross_origin()
@app.route('/', methods=['GET'])
def informacion_nodo():
    '''
    Este servicio permite conocer la informacion del nodo

    .. parsed-literal::
        # añadir numero
        curl http://direccion:puerto/

    '''
    return jsonify(nodo.__dict__)

@cross_origin()
@app.route('/suma_de_red', methods=['POST'])
def sumar_red():

    '''
    Este servicio permite sumar la red de nodos

    .. parsed-literal::
        # añadir numero
        curl http://direccion:puerto/suma_de_red/

    '''
    
    #print("Entrada",request.json)
    parametro = dict(request.json)
    lista_vecinos_confirmados = list(parametro['nodos_sumados'])
    origen = parametro['origen_peticion']
    identificador_nodo_solicitud = parametro['identificador_solicitud']
    respuesta = {}
    
    if identificador_nodo_solicitud == '':
        nodo.es_master = True
    else:
        nodo.master_actual = identificador_nodo_solicitud

    if not controlador.validar_solicitud(identificador_nodo_solicitud, nodo):
        respuesta = controlador.obtener_suma(nodo, lista_vecinos_confirmados,origen)
        suma_r = respuesta['suma_total']
        respuesta = {'estado_solicitud':True, 'suma_total':suma_r}
        nodo.agregar_solicitud_con_respuesta(identificador_nodo_solicitud)
    else:
        respuesta = {'estado_solicitud':False, 'suma_total':0}
    nodo.es_master = False
    return respuesta

@cross_origin()
@app.route('/guardar_numero', methods=['POST'])
def anadir_numero():
    '''
    Este servicio permite añadir numeros al nodo

    .. parsed-literal::
        # añadir numero
        curl http://direccion:puerto/guardar_numero/

    '''
    print(request.form)
    respuesta = {}
    try:
        numero = request.form['numero']
        respuesta = controlador.insertar_numero(nodo,numero)
    except BadRequestKeyError as e:
        respuesta = {'Error': True, 'TypeError':'Parametro numero necesario'}
    return jsonify(respuesta)

# <--------------------------- Funciones aplicacion --------------------------->

def establecer_nodo(lista_nodos_vecinos,  ip, nombre, nodo_hash, port):
    '''
    Esta funcion establece los parametros para iniciar el nodo

    :param lista_nodos_vecinos:
    :type lista_nodos_vecinos:
    :param ip:
    :type ip:
    :param nombre:
    :type nombre:
    :param nodo_hash:
    :type nodo_hash:
    :param port:
    :type port:
    '''
    nodo.lista_nodos_vecinos = lista_nodos_vecinos
    nodo.direccion_ip = ip
    nodo.nombre = nombre
    nodo.identificador_hash = nodo_hash
    nodo.puerto = port

def start(ip:str, port:int, lista_nodos_vecinos:list, nombre, nodo_hash, nuget):
    '''
    Función de inicio de aplicación (nodo)
    
    :param ip: la dirección ip del nodo
    :type ip: str
    :param port: el puerto donde se aloja la aplicación (nodo)
    :type port: int
    :param lista_nodos_vecinos: la lista de los nodos que conoce la aplicación
    :type lista_nodos_vecinos: list
    '''
    establecer_nodo(lista_nodos_vecinos,  ip, nombre, nodo_hash,port)
    print('Running...')
    print('-'*100)
    print(nodo)
    print('-'*100)
    app.run(ip, port, debug=nuget)
   
