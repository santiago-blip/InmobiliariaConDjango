$(document).ready(function() {
    $("#buscador").keydown((e) => {
        console.log(e.key)
        var token = document.getElementsByName("csrfmiddlewaretoken")[0].value
        buscadorAjax(e.key, token)
    });

    function buscadorAjax(buscador, token) {
        $.ajax({
            type: 'POST',
            url: "search/",
            data: { "buscador": buscador, "csrfmiddlewaretoken": token },
            success: function(data, textStatus, jqXHR) {
                console.log("Se envió: " + buscador)
            }
        });
    }
});