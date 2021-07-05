function cargar(id) {
  $.post("../../venta/" + id + "/", {
    id: id
  }, function (data) {
    console.log(data);
    $("#itemsventa").empty();
    for (producto of data) {
      if (producto["cantidad"] >= 4 && producto["promo"] == true) {
        $("#itemsventa").append('<tr>' +
                                '<td>' + producto["producto__nombre"] + '</td>' +
                                '<td class="text-success">' + Math.round(producto["producto__precio"]*0.9).toFixed(0) + '</td>' +
                                '<td>' + producto["cantidad"] + '</td>' +
                                '<td class="text-success">' + Math.round(producto["cantidad"]*(producto["producto__precio"]*0.9).toFixed(0)) + '</td>' +
                              '</tr>');
      } else {
      $("#itemsventa").append('<tr>' +
                              '<td>' + producto["producto__nombre"] + '</td>' +
                              '<td>' + producto["producto__precio"] + '</td>' +
                              '<td>' + producto["cantidad"] + '</td>' +
                              '<td>' + producto["cantidad"]*producto["producto__precio"] + '</td>' +
                            '</tr>');
      }
    }
    $(".modal").modal('show');
  });
}

function tomar(id) {
  $.post("../../venta/tomar/" + id + "/", {
  }, function (data) {
    if (data = "Ok") {
      window.location.reload();
    }
  })
}