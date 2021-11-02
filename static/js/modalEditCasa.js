var info = document.getElementById("AbrirModalEditInfo");
var img = document.getElementById("AbrirModalImg");

//MODALES
var contenedorModalesEdit = document.getElementById("contenedorModalesEdit");
var modalFormEditDatos = document.getElementById("modalFormEditDatos");
var modalFormEditImg = document.getElementById("modalFormEditImg");

//Iniciar Sesión desde menú
if (info != null) {
    info.addEventListener("click", () => {
        if (modalFormEditImg.classList.contains("modalVisible")) {
            modalFormEditImg.classList.toggle("modalVisible")
        }
        contenedorModalesEdit.classList.toggle("mostrarContenedor")
        modalFormEditDatos.classList.toggle("modalVisible")
    })
}

if (img != null) {
    img.addEventListener("click", () => {
        if (modalFormEditDatos.classList.contains("modalVisible")) {
            modalFormEditDatos.classList.toggle("modalVisible")
        }
        contenedorModalesEdit.classList.toggle("mostrarContenedor")
        modalFormEditImg.classList.toggle("modalVisible")
    })
}



window.addEventListener("click", function(e) {
    if (e.target == contenedorModalesEdit) {
        if (modalFormEditDatos.classList.contains("modalVisible")) {
            modalFormEditDatos.classList.toggle("modalVisible");
        } else if (modalFormEditImg.classList.contains("modalVisible")) {
            modalFormEditImg.classList.toggle("modalVisible");
        }
        contenedorModalesEdit.classList.toggle("mostrarContenedor");
    }
});