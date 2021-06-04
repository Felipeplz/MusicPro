function anniadir(id) {
    alert("Se añadió el producto id: " + id + " al carrito.");
    $.post("../../anniadir",{
        id
      },function(data){
          mensajeCarrito(data, id);
      });
}