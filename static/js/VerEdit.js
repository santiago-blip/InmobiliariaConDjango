var campo = document.getElementsByClassName("btnEdit");
var divImg = document.getElementById("divConElFormularioPARAcambiodeGaleria");
for (var i = 0; i < campo.length; i++) {
    campo[i].addEventListener("click", function() {
        console.log(campo[i])
        divImg[campo].classList.toggle("verEditImg");
    });
}