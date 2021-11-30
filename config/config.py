'''
Archivo config
--------------
Este modulo contiene la configuración del nodo
'''
config_numero = 3

config_nodos= [{
    'nombre_nodo':'Nodo A',
    'ip_address': 'localhost',
    'port':5200,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'localhost', 'puerto':5201},
        {'nombre_nodo':'Nodo C', 'ip':'localhost', 'puerto':5202}
    ],
    'debug':True
    },
    {
    'nombre_nodo':'Nodo B',
    'ip_address': 'localhost',
    'port':5201,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo A', 'ip':'localhost', 'puerto':5200},
        {'nombre_nodo':'Nodo C', 'ip':'localhost', 'puerto':5202},
        {'nombre_nodo':'Nodo D', 'ip':'localhost', 'puerto':5203}
    ],
    'debug':False
    },
    
    {
    'nombre_nodo':'Nodo C',
    'ip_address': 'localhost',
    'port':5202,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'localhost', 'puerto':5201},
        {'nombre_nodo':'Nodo A', 'ip':'localhost', 'puerto':5200},
        {'nombre_nodo':'Nodo D', 'ip':'localhost', 'puerto':5203}
    ],
    'debug':False
    },
    {
    'nombre_nodo':'Nodo D',
    'ip_address': 'localhost',
    'port':5203,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'localhost', 'puerto':5201},
        {'nombre_nodo':'Nodo C', 'ip':'localhost', 'puerto':5202}
    ],
    'debug':False
    },
]