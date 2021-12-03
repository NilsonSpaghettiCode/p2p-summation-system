/* 
Archivo de Configuración
*/ 
export const config ={
    "Nodo_A":{"ip_direccion":"localhost:5200","estado":false},
    "Nodo_B":{"ip_direccion":"0.0.0.0:5201","estado":false},
    "Nodo_C":{"ip_direccion":"0.0.0.0:5202","estado":false},
    "Nodo_D":{"ip_direccion":"0.0.0.0:5203","estado":false}   
}
export const endpoints = {
    "agregar_numero":{"value":"/guardar_numero", "metodos":['POST']},
    "suma_red":{"value":"/suma_de_red", "metodos":['POST']},
    "info_nodo":{"value":"/", "metodos":['GET']}
}

