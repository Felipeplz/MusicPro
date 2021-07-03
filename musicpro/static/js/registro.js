$("#btnRegistro").click(function() {
    let user = $("#email").val(),
        pass = $("#pass").val(),
        suscrito = $("#checkPromociones").val();
    $.ajax({
        url : "../../registrar/",
        type: "POST",
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, user, pass, suscrito},
        dataType : "html",
        success: function( data ){
            if (data != "Ok") {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: data
                })
            } else {
                window.location.replace("../../catalogo/");
            }
        }
    });
})

$("#modalRegistro").on('hidden.bs.modal', function(e) {
    window.location.replace("../../catalogo/");
})

$(function () {
    $("#checkPromociones").change(function() {
        $(this).val($(this).is(':checked'));
    });
})