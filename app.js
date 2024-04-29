let ubicacionPrincipal = window.pageYOffset;
window.onscroll = function(){


    let Desplazamiento = window.pageYOffset;
    if(ubicacionPrincipal >= Desplazamiento){
        document.getElementById('navbar').style.top = '0px';

    }
    else{
        document.getElementById('navbar').style.top = '-200px';

    }
    ubicacionPrincipal = Desplazamiento;
}