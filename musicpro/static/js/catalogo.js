function anniadir(id) {
  $.post("../../carrito/add/",{
      id:id
    },function(data){
        window.location.replace("../../carrito");
    });
}