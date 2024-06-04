document.addEventListener('DOMContentLoaded', async () => {
    let btnbuscar = document.getElementById('buscar');
    let texto = document.getElementById('texto');
    const resultadoshtml = document.getElementById('resultados');


    btnbuscar.addEventListener('click', async (e) => {
        e.preventDefault();
        const busqueda = texto.value;
        const url = `https://steam-api7.p.rapidapi.com/search?query=${busqueda}&limit=10`;
        const options = {
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': 'b46a0e4d55mshca3171d7e5c8cdbp113f01jsn899b0be4fbd7',
                'X-RapidAPI-Host': 'steam-api7.p.rapidapi.com'
            }
        };

        try {
            const response = await fetch(url, options);
            const data = await response.json(); // convertir a JSON
            mostrarResultados(data.results); 
        } catch (error) {
            console.error(error);
        }
    });

    function mostrarResultados(resultados) {
        resultadoshtml.innerHTML = ''; //limpiar
        //iterar por cada resultado
        resultados.forEach(resultado => {
            
            let resultadoElement = document.createElement('div');
            resultadoElement.textContent = resultado.name;
            
            resultadoshtml.appendChild(resultadoElement);
        });
    
        
        $('#resultadosModal').modal('show');
    }

    let btninfo=document.getElementById('boton-info')
   //mi api
 
    
    
});

