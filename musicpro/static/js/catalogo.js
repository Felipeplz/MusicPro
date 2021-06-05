function anniadir(id) {
    $.post("../../login/",{
        usuario:$("#usuario").val(),
        contraseña:$("#contraseña").val()
      },function(data){
        window.location.reload();
      });
}