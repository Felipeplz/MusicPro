$("#ingresar").submit(function (e) {
  console.log(login);
  if (login == false) {
    e.preventDefault();
    let mail = $("#usuario").val(),
    pass = $("#contraseña").val();
    console.log("enviando post");
    $.post("../../trylogin/", {
      mail,
      pass
    }, function (data) {
      if (data != "Ok") {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: data
        });
        return false;
      } else {
        login = true;
        console.log("reenviando submit");
        $("#ingresar").submit();
      }
    })
  }
})