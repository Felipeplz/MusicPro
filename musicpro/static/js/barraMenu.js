function login() {
  $.post("../../carrito/add/", {
    id: id
  }, function (data) {
    window.location.replace("../../carrito");
  });
}