document.addEventListener('DOMContentLoaded', () => {


    const fecha_juego = new Date('06/13/2024 0:01 AM');

    const dias = document.querySelector('#days');
    const horas = document.querySelector('#hours');
    const minutos = document.querySelector('#minutes');
    const segundos = document.querySelector('#seconds');
    
    const milisegundos_segundo = 1000;
    const milisegundos_minuto = milisegundos_segundo * 60;
    const milisegundos_hora= milisegundos_minuto * 60;
    const milisegundos_dias = milisegundos_hora* 24

    

    
    function updateCountdown() {
        
        const now = new Date()
        const duracion = fecha_juego - now;
        const dias_restantes = Math.floor(duracion / milisegundos_dias);
        const horas_restantes = Math.floor((duracion % milisegundos_dias) / milisegundos_hora);
        const minutos_restantes = Math.floor((duracion % milisegundos_hora) / milisegundos_minuto);
        const segundos_restantes = Math.floor((duracion % milisegundos_minuto) / milisegundos_segundo);
        
        dias.textContent = dias_restantes;
        horas.textContent = horas_restantes;
        minutos.textContent =  minutos_restantes;
        segundos.textContent = segundos_restantes;
    }

   
    updateCountdown();
    
    setInterval(updateCountdown,1000);

    

});

