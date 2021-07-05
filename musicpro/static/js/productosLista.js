function modalNuevo() {
  $("#modalNuevo").modal('show');
}

function cargar(id) {
  $.post("../../producto/" + id + "/",{
      id:id
    },function(data){
      $("#modalModificar #txt_nombre").val(data[0]["nombre"]);
      $("#modalModificar #txt_tipo").val(data[0]["tipo"]);
      $("#modalModificar #txt_subtipo").val(data[0]["subtipo"]);
      $("#modalModificar #txt_marca").val(data[0]["marca"]);
      $("#modalModificar #txt_precio").val(data[0]["precio"]);
      $("#modalModificar #txt_stock").val(data[0]["stock"]);
      $("#modalModificar #img_producto").attr("src","/media/" + data[0]["foto"]);
      $("#modalModificar #cmb_categoria").val(data[0]["categoria"]);
      $("#modalModificar #txa_descripcion").val(data[0]["descripcion"]);
      $("#formModificar").attr("action","../../producto/" + id + "/editar/")
      $("#modalModificar").modal('show');
    });
}

$("#formNuevo").submit(function(e) {
  $("#modalNuevo #txt_precio").val($("#modalNuevo #txt_precio").val().replace('.',''));
  let nombre = $("#modalNuevo #txt_nombre").val(),
      tipo = $("#modalNuevo #txt_tipo").val(),
      subtipo = $("#modalNuevo #txt_subtipo").val(),
      marca = $("#modalNuevo #txt_marca").val(),
      precio = $("#modalNuevo #txt_precio").val(),
      stock = $("#modalNuevo #txt_stock").val(),
      descripcion = $("#modalNuevo #txa_descripcion").val(),
      foto = $("#modalNuevo #fil_foto").val();
  if (nombre.trim().length == 0 || tipo.trim().length == 0 || subtipo.trim().length == 0 || marca.trim().length == 0 || precio.trim().length == 0 || stock.trim().length == 0 || descripcion.trim().length == 0 || foto.trim().length == 0) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Favor ingrese todos los campos solicitados."
    });
    return false;
  }
  if ($.inArray(rol.trim(), ['Instrumentos de Cuerdas','Percusión','Amplificadores','Accesorios varios',]) == -1) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese una categoría válida."
    });
    return false;
  } 
});

$("#formModificar").submit(function(e) {
  $("#formModificar #txt_precio").val($("#formModificar #txt_precio").val().replace('.',''));
  let nombre = $("#modalModificar #txt_nombre").val(),
      tipo = $("#modalModificar #txt_tipo").val(),
      subtipo = $("#modalModificar #txt_subtipo").val(),
      marca = $("#modalModificar #txt_marca").val(),
      precio = $("#modalModificar #txt_precio").val(),
      stock = $("#modalModificar #txt_stock").val(),
      descripcion = $("#modalModificar #txa_descripcion").val();
  if (nombre.trim().length == 0 || tipo.trim().length == 0 || subtipo.trim().length == 0 || marca.trim().length == 0 || precio.trim().length == 0 || stock.trim().length == 0 || descripcion.trim().length == 0) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Favor ingrese todos los campos solicitados."
    });
    return false;
  }
  if ($.inArray(rol.trim(), ['Instrumentos de Cuerdas','Percusión','Amplificadores','Accesorios varios',]) == -1) {
    e.preventDefault();
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: "Ingrese una categoría válida."
    });
    return false;
  } 
});