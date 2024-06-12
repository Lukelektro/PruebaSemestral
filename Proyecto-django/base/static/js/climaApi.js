document.addEventListener('DOMContentLoaded', function() {

    const apiKey = '5cfa40e09cdcdcf65068738593c1885f';
    const ciudad1 = 'Viña del mar';
    const ciudad2 = 'Quilpue';
    const pais = 'CL';

    const url1 = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad1},${pais}&appid=${apiKey}&units=metric`;
    const url2 = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad2},${pais}&appid=${apiKey}&units=metric`;

    fetch(url1) // fetch clima de viña
        .then(response => { 
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log('Data:', data);
            document.getElementById('temp1').textContent = data.main.temp;
        })
        .catch(error => console.error('Error fetching data: ', error

    ));

    fetch(url2)  // fetch clima de quilpue
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log('Data:', data); 
            document.getElementById('temp2').textContent = data.main.temp;
        })
        .catch(error => console.error('Error fetching data: ', error

    ));

    
});


