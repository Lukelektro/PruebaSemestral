
$(document).ready(function() {
    // Función para cambiar el intervalo de tiempo del carousel
    $('.carousel').carousel({
        interval: 20
    });

    // Permite a la navbar salirse de los bordes de la pantalla
    let ubicacionPrincipal = $(window).scrollTop();

    $(window).scroll(function() {
        let Desplazamiento = $(this).scrollTop();
        if (ubicacionPrincipal >= Desplazamiento) {
            $('#navbar').css('top', '0px');
        } else {
            $('#navbar').css('top', '-530px');
        }
        ubicacionPrincipal = Desplazamiento;
    });

    // Permite que el botón de ir arriba aparezca al hacer scroll
    $('[data-toggle="popover"]').popover();

    // Manejo del modal
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').focus();
    });
});

