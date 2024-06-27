const button = document.querySelector("#enviar");

/* Callback function */
function alerta() {
    const alerta = document.getElementById("succes");
    alerta.className="alert alert-success text-center";
}

/* Event listener */
button.addEventListener("click", alerta, false);