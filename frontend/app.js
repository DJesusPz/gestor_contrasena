function consulta_general(){
    let url = "http://127.0.0.1:5000/";
    fetch(url)
    .then( response => response.json())
    .then( data => visualizar(data) )
    .catch( error => console.log(error) )
    const visualizar = (data) => {
    console.log(data)
    let b = ""
    for (var i = 0; i < data.baul.length; i++) {
    console.log(i,data.baul[i].Plataforma)
    console.log(i,data.baul[i].usuario)
    console.log(i,data.baul[i].clave)
    b+=`<tr><td>${data.baul[i].id_baul}</td><td>${data.baul[i].plataforma}</td><td>${data.baul[i].usuario}</td><td>${data.baul[i].clave}</td><td><button type='button' class="btn btn-
    info" onclick="location.href = 'edit.html?variable1=${data.baul[i].id_baul}'"> <img src='imagenes/edit.png' height ='30' width='30'/></button>
    <button type='button' class="btn btn-warning" onclick="eliminar(${data.baul[i].id_baul})"> <img src='imagenes/delete.png' height ='30' width='30'/></button></tr>`}
    document.getElementById('data').innerHTML = b }}

function eliminar(id){
    let url = "http://127.0.0.1:5000/eliminar/"+id;
    fetch(url, {
    method: 'DELETE',
    })
    .then( response => response.json() )
    .then(res => visualizar(res) )
    const visualizar = (res) => {
    swal("Mensaje", "Registro "+ res.mensaje+" exitosamente",
    "success").then(() => {
    swal(window.location.reload());
    });
    }}

function registrar(){
    let url = "http://127.0.0.1:5000/registro/";
    plat=document.getElementById("plataforma").value
    usua=document.getElementById("usuario").value
    clav=document.getElementById("clave").value
var data = { "Plataforma": plat,
                "usuario":usua,
                "clave":clav
};
console.log(data)
fetch(url, {
    method: "POST", // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers: {"Content-Type": "application/json",
},
})
.then((res) => res.json())
.catch((error) => console.error("Error:", error))
.then((response) => visualizar(response));
const visualizar = (response) => {
console.log("Success:", response)
if (response.mensaje=="Error")
    swal("Mensaje", "Error en el registro", "error")
else
    swal("Mensaje", "Registro agregado exitosamente", "success")
} }

function consulta_individual(id){
// alert(id)
let url = "http://127.0.0.1:5000/consulta_individual/"+id;
fetch(url)
.then( response => response.json())
.then( data => visualizar(data) )
.catch( error => console.log(error) )
const visualizar = (data,id) => {
console.log(data)
//
document.getElementById("idbaul").value=data.baul[i].id_baul
document.getElementById("plataforma").value=dat
a.baul.Plataforma
document.getElementById("usuario").value=data.b
aul.usuario
document.getElementById("clave").value=data.bau
l.clave
}
}

function modificar(id){
    let url = "http://127.0.0.1:5000/actualizar/"+id;
    plat=document.getElementById("plataforma").value
    usua=document.getElementById("usuario").value
    clav=document.getElementById("clave").value
var data = { "Plataforma":plat,
            "usuario":usua,
            "clave":clav
};
console.log(data)
fetch(url, {
method: "PUT", // or 'PUT'
body: JSON.stringify(data), // data can be `string` or {object}!
headers: {
    "Content-Type": "application/json",
},
})
.then((res) => res.json())
.catch((error) => console.error("Error:", error))
.then((response) => visualizar(response));
const visualizar = (response) => {
    console.log("Success:", response)
    if (response.mensaje=="Error")
    swal("Mensaje", "Error en el registro", "error")
    else
    swal("Mensaje", "Registro actualizado exitosamente", "success")
}}