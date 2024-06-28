document.addEventListener('DOMContentLoaded', async () => {

    let btnenviar= document.getElementById('btnenviar')
    let  nombre=document.getElementById('nombre')
    let  correo=document.getElementById('correo')
    let  asunto=document.getElementById('asunto')
    let  mensaje=document.getElementById('mensaje')
    
    btnenviar.addEventListener('click',async (e)=>{
        e.preventDefault();
        const url = 'https://mail-sender-api1.p.rapidapi.com/';
    const options = {
        method: 'POST',
        headers: {
            'x-rapidapi-key': 'b46a0e4d55mshca3171d7e5c8cdbp113f01jsn899b0be4fbd7',
            'x-rapidapi-host': 'mail-sender-api1.p.rapidapi.com',
            'Content-Type': 'application/json'
        },
        body:JSON.stringify( {
            sendto: 'maximiliano.duran114@gmail.com',
            name: nombre.value,
            replyTo: 'maximiliano.duran114@gmail.com',
            ishtml: 'false',
            title: asunto.value,
            body: mensaje.value
        })
    };
    
    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
    
    })
    });