console.log("ONLY");

function cerrar_sesion(event) {
  event.preventDefault();
  var logOut = document.getElementById("logout-form");
  logOut.submit();
}
