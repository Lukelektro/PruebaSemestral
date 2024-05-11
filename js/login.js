$(document).ready(function(){
    $("#form-contacto").submit(function(event){

        event.preventDefault();

        if (this.checkValidity() === false) { //verifica si todos los campos del formulario son válidos
            event.stopPropagation(); // previene que el evento se propague
        } else { // si todos los campos son válidos
            // Aquí puedes redirigir al usuario, mostrar un mensaje de éxito, etc.
        }

        $(this).addClass('was-validated'); // agrega la clase de bootstrap para mostrar los mensajes de validación
    });
});