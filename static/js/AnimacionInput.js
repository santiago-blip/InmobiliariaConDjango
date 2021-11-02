var inputs = document.getElementsByClassName("divSessioninput")
if (inputs != null) {
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener("keyup", function() {
            if (this.value.length >= 1) {
                this.nextElementSibling.classList.add("fijar");
            } else {
                this.nextElementSibling.classList.remove("fijar");
            }
        })
    }
}

var inputsRegistro = document.getElementsByClassName("inputFormRegistro")
if (inputsRegistro != null) {
    for (var i = 0; i < inputsRegistro.length; i++) {
        inputsRegistro[i].addEventListener("keyup", function() {
            if (this.value.length >= 1) {
                this.nextElementSibling.classList.add("fijar");
            } else {
                this.nextElementSibling.classList.remove("fijar");
            }
        })
    }
}

var inputFormRegistroCasa = document.getElementsByClassName("inputFormRegistroCasa")
if (inputFormRegistroCasa != null) {
    for (var i = 0; i < inputFormRegistroCasa.length; i++) {
        inputFormRegistroCasa[i].addEventListener("keyup", function() {
            if (this.value.length >= 1) {
                this.nextElementSibling.classList.add("fijar");
            } else {
                this.nextElementSibling.classList.remove("fijar");
            }
        })
    }
}