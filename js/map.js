
$(document).ready(function(){

    initMap();
    initMap2();
    
});


let map1;
let map2;


// viña del mar -33.01470981444226, -71.54383930229129

function initMap() {

    const location1 = { lat: -33.01470981444226, lng: -71.54383930229129};

    map1 = new google.maps.Map(document.getElementById("map"), {
        center: location1,
        zoom: 15,
    });

    const marker = new google.maps.Marker({
        position: location1,
        map: map1,
        title: "locacion de la empresa"
    });
}

// Quilpue -33.03957443720588, -71.47659704456483
function initMap2() {
    const location2 = { lat: -33.03957443720588, lng: -71.47659704456483}; // Cambia estas coordenadas

    map2 = new google.maps.Map(document.getElementById("map2"), {
        center: location2,
        zoom: 15,
    });

    const marker = new google.maps.Marker({
        position: location2,
        map: map2,
        title: "Nueva ubicación"
    });
}





// API KEY = AIzaSyCDbHPBuZkWfS1x2-HAklCMeaFEkYhOq2I