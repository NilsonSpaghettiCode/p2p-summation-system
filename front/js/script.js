import { config, endpoints } from "./config.js";

//Nodo seleccionado
let nodo = ""
//Inputs de suma
const entrada_numero = document.getElementById('number')
let numero_nodo = document.getElementById('nodo')

//Etiquetas de total
const etiqueta_suma_total = document.getElementById('total_sum')
const etiqueta_suma_a = document.getElementById('suma_nodo_a')
const etiqueta_suma_b = document.getElementById('suma_nodo_b')
const etiqueta_suma_c = document.getElementById('suma_nodo_c')
const etiqueta_suma_d = document.getElementById('suma_nodo_d')

//Botones
const btn_agregar_numero = document.getElementById('add_number')
const btn_suma_total = document.getElementById('sum_network')


//Colores
const GREY = "rgb(160 174 192)"
const GREEN = "green"
const GREEN_LIGHT = "rgb(198, 246, 213)"
const RED = "red"
const RED_LIGHT = "rgb(254, 178, 178)"

//Estados
const INACTIVE ="Inactive"
const ACTIVE = "Active"

//Dom resultado
const table_info_nodo = document.getElementById("node_info")
const table_suma_nodos = document.getElementById("current_result")
const text_area_sum_nodo = document.getElementById("node_current_sum")
const text_area_numbers = document.getElementById("node_current_numbers")

btn_agregar_numero.addEventListener("click", (e) => {
    nodo = ""
    let numero_parsed = parseInt(entrada_numero.value)
    if (!isNaN(numero_parsed)) {
        establecer_nodo(numero_nodo.value)
        agregar_numero(numero_parsed)
        mostrar_nodo_info()
    } else {
        alert("Ingrese numeros en el Input number")
    }

})

btn_suma_total.addEventListener("click", (e) => {
    let numero_parsed = parseInt(numero_nodo.value)
    if (!isNaN(numero_parsed)) {
        establecer_nodo(numero_nodo.value)
        suma_red()
        mostrar_nodo_info()
    } else {
        alert("Ingrese numeros en el Input number")
    }
})

const agregar_numero = (numero) => {
    var formdata = new FormData()
    formdata.append("numero", numero)
    console.log(formdata)
    consumir_servicio(nodo, endpoints.agregar_numero.value, formdata, endpoints.agregar_numero.metodos[0], response_service_agregar_numero, error_solicitud)
}

const response_service_agregar_numero = (resultado) => {
    console.log(resultado)
    //establecer_nodo(numero_nodo.value)
    //alert(`Numero agregado: ${resultado['estado']}`)
 
}

const mostrar_nodo_info = ()=>
{
    console.log(endpoints.info_nodo.metodos[0], nodo, endpoints.info_nodo.value)
    consumir_servicio(nodo,endpoints.info_nodo.value,"",endpoints.info_nodo.metodos[0],establecer_datos_nodo,mostrar_nodo_info_error)
}

const establecer_datos_nodo =(resultado)=>
{
    console.log(resultado)
    table_info_nodo.style.display = "block"
    text_area_sum_nodo.textContent = resultado['suma_nodo']
    text_area_numbers.textContent = resultado['lista_numeros']
}

const mostrar_nodo_info_error = (error) => {
    table_info_nodo.style.display = "none"
}

const suma_red = () => {
    let raw = JSON.stringify({
        "nodos_sumados": [],
        "origen_peticion": "",
        "identificador_solicitud": ""
      })
      JSON.stringify()

    consumir_servicio(nodo, endpoints.suma_red.value, raw, endpoints.suma_red.metodos[0], mostrar_resultado_suma, mostrar_resultado_suma_error)
}

const mostrar_resultado_suma = (resultado) => {
    table_suma_nodos.style.display = "block"
    etiqueta_suma_total.textContent = resultado['suma_total']
    etiqueta_suma_a.textContent = resultado['']
    etiqueta_suma_b.textContent = resultado['']
    etiqueta_suma_c.textContent = resultado['']
    etiqueta_suma_d.textContent = resultado['']
    
}

const mostrar_resultado_suma_error = (error) => {
    alert('Error: '+error)
    table_suma_nodos.style.display = "none"
}

const obtener_nodo = () => {

}

const cambiar_estados_nodos = (id, color, estado) => {
    let lb_nodo_n = document.getElementById(id)
    lb_nodo_n.textContent = estado
    lb_nodo_n.style.backgroundColor = color
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
                cambiar_estados_nodos("lb_nodo_a", GREEN_LIGHT, ACTIVE)
                break;
            case 2:
                nodo = config.Nodo_B.ip_direccion
                establecer_nodo_color("nodo_b",GREEN)
                cambiar_estados_nodos("lb_nodo_b", GREEN_LIGHT, ACTIVE)
                break;
            case 3:
                nodo = config.Nodo_C.ip_direccion
                establecer_nodo_color("nodo_c",GREEN)
                cambiar_estados_nodos("lb_nodo_c", GREEN_LIGHT, ACTIVE)
                break;
            case 4:
                nodo = config.Nodo_D.ip_direccion
                establecer_nodo_color("nodo_d",GREEN)
                cambiar_estados_nodos("lb_nodo_d", GREEN_LIGHT, ACTIVE)
                break;
            default:
                alert("Digite un nodo valido")

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

const consumir_servicio = (direccion, endpoint, body, metodo, function_response, function_error) => {
    let requestOptions = generar_requestOptions(metodo, body)
    let url = generar_url(direccion, endpoint)
    console.log(url)
    console.log(requestOptions)
    fetch(url, requestOptions)
        .then(response => response.json())
        .then(result => function_response(result)) //Implementar
        .catch(error => function_error(error));
}

const error_solicitud=()=>
{
    let id_nodo = encontrar_boton(numero_nodo)
    establecer_nodo_color(id_nodo, RED)   
    cambiar_estados_nodos((`lb_${id_nodo}`), RED_LIGHT, INACTIVE)
}

const encontrar_boton=(numero_nodo)=>
{
    let id = ""
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
    let request_option = ""
    
    if (formdata === "") {
        request_option = { method: metodo, redirect: "follow" }
    }else if(typeof(formdata)==='string'){ 
        let header = new Headers()
        header.append("Content-Type", "application/json")
        request_option = { method: metodo, headers:header, body: formdata, redirect: "follow" }
    }else{
        request_option = { method: metodo, body: formdata, redirect: "follow" }
    }
    console.log(request_option)
    return request_option
}

const generar_url = (direccion, endpoint) => {
    return `http://${direccion}${endpoint}`
}

