
document.addEventListener('DOMContentLoaded', function() {

    
    $("#form-contacto").submit(function(event){

        event.preventDefault(); // previene que el formulario se envíe

        if (this.checkValidity() === false) { //verifica si todos los campos del formulario son válidos
            event.stopPropagation(); // previene que el evento se propague
        } else { // si todos los campos son válidos
            $('#successModal').modal('show'); // Aparece el modal
        }

        $(this).addClass('was-validated'); // agrega la clase de bootstrap para mostrar los mensajes de validación
    });

    
});