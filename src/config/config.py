'''
Archivo config
--------------
Este modulo contiene la configuración del nodo
'''
config_numero = 0

config_nodos= [{
    'nombre_nodo':'Nodo A',
    'ip_address': '172.18.0.22',
    'port':5200,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'172.18.0.24', 'puerto':5201},
        {'nombre_nodo':'Nodo C', 'ip':'172.18.0.26', 'puerto':5202}
    ],
    'debug':True
    },
    {
    'nombre_nodo':'Nodo B',
    'ip_address': '172.18.0.24',
    'port':5201,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo A', 'ip':'172.18.0.22', 'puerto':5200},
        {'nombre_nodo':'Nodo C', 'ip':'172.18.0.26', 'puerto':5202},
        {'nombre_nodo':'Nodo D', 'ip':'172.18.0.28', 'puerto':5203}
    ],
    'debug':False
    },
    
    {
    'nombre_nodo':'Nodo C',
    'ip_address': '172.18.0.26',
    'port':5202,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'172.18.0.24', 'puerto':5201},
        {'nombre_nodo':'Nodo A', 'ip':'172.18.0.22', 'puerto':5200},
        {'nombre_nodo':'Nodo D', 'ip':'172.18.0.28', 'puerto':5203}
    ],
    'debug':False
    },
    {
    'nombre_nodo':'Nodo D',
    'ip_address': '172.18.0.28',
    'port':5203,
    'nodos_conocidos':[
        {'nombre_nodo':'Nodo B', 'ip':'172.18.0.24', 'puerto':5201},
        {'nombre_nodo':'Nodo C', 'ip':'172.18.0.26', 'puerto':5202}
    ],
    'debug':False
    },
]