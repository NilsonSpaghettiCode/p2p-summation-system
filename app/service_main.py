from flask import Flask
app = Flask(__name__)

@app.route('/')
def informacion_nodo():
    pass
@app.route('suma_de_red', methods=['GET'])
def sumar_red():
    pass
@app.route('guardar_numero', methods=['POST'])
def anadir_numero():
    pass



def start(ip:str, port:int):
    print('Running...')
    app.run(ip, port, debug=True)
