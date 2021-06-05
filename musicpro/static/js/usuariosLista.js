function modalNuevo() {
  $("#modalNuevo").modal('show');
}

function cargar(id) {
  $.post("../../usuario/" + id + "/",{
      id:id
    },function(data){
      console.table(data);
      $("#modalModificar #txt_nombre").val(data[5]);
      $("#modalModificar #txt_mail").val(data[1]);
      $("#modalModificar #txt_rut").val(data[3]);
      $("#modalModificar #txt_dv").val(data[4]);
      $("#modalModificar #txt_fono").val(data[6]);
      $("#modalModificar #txt_direccion").val(data[7]);
      $("#modalModificar #cmb_rol").val(data[8]);
      $("#modalModificar").modal('show');
      $("#formModificar").attr("action","../../usuario/" + id + "/editar/")
    });
}