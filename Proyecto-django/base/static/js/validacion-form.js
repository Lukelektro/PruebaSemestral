$(document).ready(function () {
    
    // Selecciona el formulario usando la clase 'needs-validation' y maneja el evento 'submit'
    $('.needs-validation').on('submit', function (event) {
      if (!this.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
  
      $(this).addClass('was-validated');
    });
  });