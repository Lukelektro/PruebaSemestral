
/* funcion para cambiar el intervalo de tiempo del carousel */
$(document).ready(function(){

    $('.carousel').carousel({
      interval: 2000
    });
    
  });


// Permite a la navbar salirse de los bordes de la pantalla
let ubicacionPrincipal = window.pageYOffset;

// Permite que la navbar se oculte al hacer scroll hacia abajo y aparezca al hacer scroll hacia arriba
window.onscroll = function () {
    let Desplazamiento = window.pageYOffset;
    if (ubicacionPrincipal >= Desplazamiento) {
        document.getElementById('navbar').style.top = '0px';
    }
    else {
        document.getElementById('navbar').style.top = '-530px';
    }
    ubicacionPrincipal = Desplazamiento;
}

// Permite que el boton de ir arriba aparezca al hacer scroll
$(function () {
    $('[data-toggle="popover"]').popover()
})

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
myInput.focus()
})
