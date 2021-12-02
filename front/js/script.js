import { config, endpoints } from "./config.js";

let nodo = config.Nodo_A.ip_direccion
//Inputs de suma
const entrada_numero = document.getElementById('number')
let numero_nodo = document.getElementById('nodo')
//Etiquetas de total
const etiqueta_suma_total = document.getElementById('total_sum')

//Botones
const btn_agregar_numero = document.getElementById('add_number')
const btn_suma_total = document.getElementById('sum_network')

//Colores
const GREY = "rgb(160 174 192)"
const GREEN = "green"
const RED = "red"

btn_agregar_numero.addEventListener("click", (e) => {
    establecer_nodo(numero_nodo.value)
    let numero_parsed = parseInt(entrada_numero.value)
    if (!isNaN(numero_parsed)) {
        agregar_numero(numero_parsed)
    } else {
        alert("Ingrese numeros en el Input number")
    }

})

btn_suma_total.addEventListener("click", (e) => {
    console.log("Holaaaaa banda")
})

const agregar_numero = (numero) => {
    var formdata = new FormData()
    formdata.append("numero", numero)
    console.log(formdata)
    consumir_servicio(nodo, endpoints.agregar_numero.value, formdata, endpoints.agregar_numero.metodos[0], response_service_agregar_numero)
}

const response_service_agregar_numero = (resultado) => {
    console.log(resultado)
    alert(`Numero agregado: ${resultado['estado']}`)
}

const cambiar_nodo = (nodo) => {

}

const suma_red = (numero) => {

}

const obtener_nodo = () => {

}

const consultar_estado_nodos = () => {

}

const establecer_nodo = (numero_nodo) => {
    let numero_persed = parseInt(numero_nodo)
    console.log(numero_nodo)
    if (isNaN(numero_persed)) {
        alert("Ingrese un nodo válido")
    } else {
        establecer_nodo_color_default()
        switch (numero_persed) {
            case 1:
                nodo = config.Nodo_A.ip_direccion
                establecer_nodo_color("nodo_a", GREEN)
                break;
            case 2:
                nodo = config.Nodo_B.ip_direccion
                establecer_nodo_color("nodo_b",GREEN)

                break;
            case 3:
                nodo = config.Nodo_C.ip_direccion
                establecer_nodo_color("nodo_c",GREEN)

                break;
            case 4:
                nodo = config.Nodo_D.ip_direccion
                establecer_nodo_color("nodo_d",GREEN)

                break;
            default:
                establecer_nodo_color("nodo_a",GREEN)
                nodo = config.Nodo_A.ip_direccion

                break;
        }
    }
}

const establecer_nodo_color = (id, color) => {
    let dom_btn = document.getElementById(id)
    dom_btn.style.backgroundColor = color
}
const establecer_nodo_color_default = ()=>
{
    establecer_nodo_color("nodo_a", GREY)
    establecer_nodo_color("nodo_b", GREY)
    establecer_nodo_color("nodo_c",GREY)
    establecer_nodo_color("nodo_d",GREY)
}



const consumir_servicio = (direccion, endpoint, body, metodo, function_response) => {
    let requestOptions = generar_requestOptions(metodo, body)
    let url = generar_url(direccion, endpoint)
    console.log(url)
    fetch(url, requestOptions)
        .then(response => response.json())
        .then(result => function_response(result)) //Implementar
        .catch(error => establecer_nodo_color(encontrar_boton(numero_nodo), RED));
}

const encontrar_boton=(numero_nodo)=>
{
    let id = "nodo_a"
    switch (numero_nodo.value) {
        case "1":
            id = "nodo_a"
            break;
        case "2":
            id = "nodo_b"
            break;
    
        case "3":
            id = "nodo_c"
            break;
    
        case "4":
            id = "nodo_d"
            break;
    
        default:
            
            break;
    }
    return id
}
const generar_requestOptions = (metodo, formdata) => {
    let headers = new Headers()
    headers.append("Content-Type", "application/json")
    return { method: metodo, body: formdata, redirect: "follow" }
}

const generar_url = (direccion, endpoint) => {
    return `http://${direccion}${endpoint}`
}