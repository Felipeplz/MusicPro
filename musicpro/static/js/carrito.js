function quitar(id) {
    $.post("../../carrito/remove/",{
        id:id
      },function(data){
          window.location.reload();
      });
}

function cambiarStock(id) {
    $.post("../../carrito/edit/",{
        id:id,
        cantidad:$("#inlineFormCustomSelectPref").val()
      },function(data){
          window.location.reload();
      });
}