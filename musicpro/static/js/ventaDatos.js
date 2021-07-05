$('[data-toggle="collapse"]').on('click', function (e) {
  if ($(this).parents('.accordion').find('.collapse.show')) {
    var idx = $(this).index('[data-toggle="collapse"]');
    if (idx == $('.collapse.show').index('.collapse')) {
      e.stopPropagation();
    }
  }
});

$("#formVenta").submit(function (e) {
  let direccion = $("#direccion").val(),
    comuna = $("#comuna").val(),
    sucursal = $("#sucursal").val(),
    domicilio = $("#despachoDomicilio").is(':checked')
    tipoPago = $("#pago .form-check-input:checked").val();
  if (domicilio) {
    if(comuna == null || domicilio.trim().lenght == 0) {
      e.preventDefault();
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: "Favor ingrese todos los campos solicitados."
      });
      return false;
    }
  } else {
    if(sucursal == null) {
      e.preventDefault();
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: "Favor ingrese todos los campos solicitados."
      });
      return false;
    }
  }
  if (tipoPago != "webpay") {
    e.preventDefault();
    $("#modalTransferencia").modal('show');
  } else {
    $.post("../../datosVenta/", {
      direccion,
      domicilio,
      sucursal,
      comuna
    }, function (data) {
      window.location.reload();
    });
  }
});

$("#modalTransferencia").on('hidden.bs.modal', function (e) {
  $.post("../../transferencia/", {
  }, function (data) {
    window.location.reload();
  });
});