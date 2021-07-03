function modalNuevo() {
  $("#modalNuevo").modal('show');
}

function cargar(id) {
  $.post("../../usuario/" + id + "/",{
      id:id
    },function(data){
      console.log(data);
      $("#modalModificar #txt_nombre").val(data[0]["nombre"]);
      $("#modalModificar #txt_mail").val(data[0]["mail"]);
      $("#modalModificar #txt_rut").val(data[0]["rut"]);
      $("#modalModificar #txt_dv").val(data[0]["dv_rut"]);
      $("#modalModificar #txt_fono").val(data[0]["telefono"]);
      $("#modalModificar #txt_direccion").val(data[0]["direccion"]);
      $("#modalModificar #cmb_rol").val(data[0]["rol"]);
      $("#modalModificar").modal('show');
      $("#formModificar").attr("action","../../usuario/" + id + "/editar/")
    });
}