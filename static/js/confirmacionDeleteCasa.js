$(document).ready(function() {
    $(".btnDelete").click(function() {
        var id = $(this).parent().find("#inputId").val();
        swal({
            title: "¿Seguro que quiere eliminar la casa?",
            text: "Se eliminará la casa de la página.",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                eliminar(id);
            } else {
                swal("No se eliminó la casa");
            }
        });
    });

    function eliminar(id) {
        $.ajax({
            type: 'GET',
            url: "/eliminar/" + id,
            data: "id=" + id,
            success: function(data, textStatus, jqXHR) {
                swal("¡La casa ha sido eliminada!", {
                    icon: "success",
                }).then(() => {
                    parent.location.href = "/";
                });
            }
        });
    }
});