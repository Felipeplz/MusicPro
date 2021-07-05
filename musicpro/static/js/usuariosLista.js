function modalNuevo() {
  $("#modalNuevo").modal('show');
}

function cargar(id) {
  $.post("../../usuario/" + id + "/", {
    id: id
  }, function (data) {
    $("#modalModificar #txt_mail").val(data[0]["mail"]);
    $("#modalModificar #txt_rut").val(data[0]["rut"]);
    $("#modalModificar #txt_fono").val(data[0]["telefono"]);
    $("#modalModificar #txt_direccion").val(data[0]["direccion"]);
    $("#modalModificar #cmb_rol").val(data[0]["rol"]);
    $("#modalModificar").modal('show');
    $("#formModificar").attr("action", "../../usuario/" + id + "/editar/")
  });
};

$("#formNuevo").submit(function(e) {
  let mail = $("#modalNuevo #txt_mail").val(),
      rut = $("#modalNuevo #txt_rut").val(),
      rol = $("#modalNuevo #cmb_rol").val();
  const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  if ($.inArray(rol.trim(), ['Cliente','Vendedor','Contador','Bodeguero','Admin',]) == -1) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese un rol válido."
    });
    return false;
  } 
  if (mail.trim().length == 0 || rut.trim().length == 0 || rol.trim().length == 0) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Favor ingrese todos los campos solicitados."
    });
    return false;
  }
  if (!re.test(String(mail).toLowerCase())) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese un correo electrónico válido."
    });
    return false;
  }
});

$("#formModificar").submit(function(e) {
  let mail = $("#modalModificar #txt_mail").val(),
      rut = $("#modalModificar #txt_rut").val(),
      rol = $("#modalModificar #cmb_rol").val();
  const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  if ($.inArray(rol.trim(), ['Cliente','Vendedor','Contador','Bodeguero','Admin',]) == -1) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese un rol válido."
    });
    return false;
  } 
  if (mail.trim().length == 0 || rut.trim().length == 0 || rol.trim().length == 0) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Favor ingrese todos los campos solicitados."
    });
    return false;
  }
  if (!re.test(String(mail).toLowerCase())) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese un correo electrónico válido."
    });
    return false;
  }
});