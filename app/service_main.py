from flask import Flask
app = Flask(__name__)

@app.route('/')
def informacion_nodo():
    '''
    Implementar servicio
    '''
    pass
@app.route('/suma_de_red', methods=['GET'])
def sumar_red():

    '''
    Implementar servicio
    '''
    pass
@app.route('/guardar_numero', methods=['POST'])
def anadir_numero():
    '''
    Implementar servicio
    '''
    pass



def start(ip:str, port:int):
    print('Running...')
    app.run(ip, port, debug=True)
