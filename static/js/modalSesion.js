var RecuperarSesion = document.getElementById("recupLogin");
var Session = document.getElementById("log");
var sesionRecup = document.getElementById("SesionRecup");
var registro = document.getElementById("registrarseLogin");
var sesionRegistro = document.getElementById("LoginRegistro");
//MODALES
var contenedorModales = document.getElementById("contenedorModales");
var modalSesion = document.getElementById("divModalSession");
var modalRegistro = document.getElementById("divModalRegistro");
var modalRecuperar = document.getElementById("divModalRecuperar");

//Iniciar Sesión desde menú
if (Session != null) {
    Session.addEventListener("click", () => {
        if (modalRegistro.classList.contains("modalVisible")) {
            modalRegistro.classList.toggle("modalVisible")
        } else if (modalRecuperar.classList.contains("modalVisible")) {
            modalRecuperar.classList.toggle("modalVisible")
        }
        contenedorModales.classList.toggle("mostrarContenedor")
        modalSesion.classList.toggle("modalVisible")
    })
}


//Recuperar contraseña
if (RecuperarSesion != null) {
    RecuperarSesion.addEventListener("click", () => {
        if (modalSesion.classList.contains("modalVisible")) {
            modalSesion.classList.toggle("modalVisible")
        }
        modalRecuperar.classList.toggle("modalVisible")
    })
}

//Volver a iniciar Sesion desde recuperar
if (sesionRecup != null) {
    sesionRecup.addEventListener("click", () => {
        if (modalRecuperar.classList.contains("modalVisible")) {
            modalRecuperar.classList.toggle("modalVisible")
        }
        modalSesion.classList.toggle("modalVisible")
    })
}

//Pasar de login a registro 
if (registro != null) {
    registro.addEventListener("click", function() {
        if (modalSesion.classList.contains("modalVisible")) {
            modalSesion.classList.toggle("modalVisible")
        }
        modalRegistro.classList.toggle("modalVisible")
    })
}

//Registro a login
if (sesionRegistro != null) {
    sesionRegistro.addEventListener("click", function() {
        if (modalRegistro.classList.contains("modalVisible")) {
            modalRegistro.classList.toggle("modalVisible")
        }
        modalSesion.classList.toggle("modalVisible")
    })
}

window.addEventListener("click", function(e) {
    if (e.target == contenedorModales) {
        if (modalSesion.classList.contains("modalVisible")) {
            modalSesion.classList.toggle("modalVisible");
        } else if (modalRegistro.classList.contains("modalVisible")) {
            modalRegistro.classList.toggle("modalVisible");
        } else if (modalRecuperar.classList.contains("modalVisible")) {
            modalRecuperar.classList.toggle("modalVisible");
        }
        contenedorModales.classList.toggle("mostrarContenedor");
    }
});


//Mostrar contraseña
//Inputs
var inputSesion = document.getElementById("Contrasena")
    //Eyes session
var eyeSesion = document.getElementById("showPass")

if (eyeSesion !== null) {
    eyeSesion.addEventListener("click", function() {
        if (eyeSesion.classList.contains("fa-eye-slash")) {
            inputSesion.type = "text";
        } else {
            inputSesion.type = "password";
        }
        eyeSesion.classList.toggle("fa-eye-slash");
    });
}
//Mostrar contraseña Registro
//Inputs
var inputRegistro = document.getElementById("passR")
    //Eyes session
var eyeRegistro = document.getElementById("showPassR")

if (eyeRegistro !== null) {
    eyeRegistro.addEventListener("click", function() {
        if (eyeRegistro.classList.contains("fa-eye-slash")) {
            inputRegistro.type = "text";
        } else {
            inputRegistro.type = "password";
        }
        eyeRegistro.classList.toggle("fa-eye-slash");
    });
}