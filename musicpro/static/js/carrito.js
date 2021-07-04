function quitar(id) {
    $.post("../../carrito/remove/",{
        id:id
      },function(data){
          window.location.reload();
      });
}

function cambiarStock(id) {
    cantidad = $("#producto" + id).val();
    $.post("../../carrito/edit/",{
        id:id,
        cantidad:cantidad
      },function(data){
          window.location.reload();
      });
}

function limpiar(id) {
    $.post("../../carrito/limpiar/",{
        id:id
      },function(data){
          window.location.reload();
      });
}