function anniadir(id) {
  cantidad = $("#productoStock").val();
  $.post("../../carrito/add/", {
    id: id,
    cantidad: cantidad
  }, function (data) {
    window.location.replace("../../carrito");
  });
}