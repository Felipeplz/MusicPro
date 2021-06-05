function modalNuevo() {
  $("#modalNuevo").modal('show');
}

function cargar(id) {
  $.post("../../producto/" + id + "/",{
      id:id
    },function(data){
      console.table(data);
      $("#modalModificar #txt_nombre").val(data[2]);
      $("#modalModificar #txt_tipo").val(data[6]);
      $("#modalModificar #txt_subtipo").val(data[7]);
      $("#modalModificar #txt_marca").val(data[4]);
      $("#modalModificar #txt_precio").val(data[5]);
      $("#modalModificar #txt_stock").val(data[9]);
      $("#modalModificar #img_producto").attr("src","/media/" + data[3]);
      $("#modalModificar #cmb_categoria").val(data[8]);
      $("#modalModificar #txa_descripcion").val(data[10]);
      $("#formModificar").attr("action","../../producto/" + id + "/editar/")
      $("#modalModificar").modal('show');
    });
}