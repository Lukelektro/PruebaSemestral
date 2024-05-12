
/* funcion para cambiar el intervalo de tiempo del carousel */
$(document).ready(function(){

    $('.carousel').carousel({
      interval: 3000
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




