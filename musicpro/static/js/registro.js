$("#btnRegistro").click(function () {
  let user = $("#email").val(),
    pass = $("#pass").val(),
    suscrito = $("#checkPromociones").val();
  const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  if (user.trim().length == 0 || pass.trim().length == 0) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "No puede dejar campos en blanco."
    });
    return false;
  }
  if (pass.trim().length < 8) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "La contraseña debe poseer al menos 8 caracteres."
    });
    return false;
  }
  if (!re.test(String(user).toLowerCase())) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese un correo electrónico válido."
    });
    return false;
  }
  $.ajax({
    url: "../../registrar/",
    type: "POST",
    data: { csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, user, pass, suscrito },
    dataType: "html",
    success: function (data) {
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

$("#modalRegistro").on('hidden.bs.modal', function (e) {
  window.location.replace("../../catalogo/");
})

$(function () {
  $("#checkPromociones").change(function () {
    $(this).val($(this).is(':checked'));
  });
})