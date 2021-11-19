from flask import Flask
app = Flask(__name__)



def start(ip:str, port:int):
    print('Running....')
    app.run(ip, port, debug=True)
