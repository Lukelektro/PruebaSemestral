$(document).ready(function(){
    $("#form-login").submit(function(event){

        event.preventDefault();

        if (this.checkValidity() === false) { //verifica si todos los cambos del form sn validos
            event.stopPropagation(); // previene que el evento se propague
        } else { // si todos los campos son validos
            window.location.href = "index.html";
        }

        $(this).addClass('was-validated'); // agrega la clase de bootstrap para mostrar los mensajes de validacion
    });
});