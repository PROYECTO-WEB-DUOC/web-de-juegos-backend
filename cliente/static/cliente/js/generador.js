document.addEventListener('DOMContentLoaded', function() {
    
function generadorcontraseña(e) {
    e.preventDefault();
        const abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".split("");
        let resultado = '';
        for (let letras = 1; letras <= 8; letras++) {
            let random = Math.floor(Math.random() * abc.length);
            resultado += abc[random];
        }
    
        document.getElementById('contraseña').value = resultado;
        document.getElementById('confirmar_contraseña').value = resultado;
    }
 



function mostrarcontraseña(e){
    e.preventDefault();
  let mostrar = document.getElementById('contraseña');
        
        mostrar.setAttribute('type','text')
        var contraseña=document.getElementById('mostrar_contraseña')
        contraseña.style.display='none';
        var ocultar=document.getElementById('ocultar_contraseña')
        ocultar.style.display='';
   
     
}
function ocultarcontraseña(e){
    e.preventDefault();
        let mostrar = document.getElementById('contraseña');
        
        mostrar.setAttribute('type','password')
        
        var ocultar=document.getElementById('ocultar_contraseña')
        ocultar.style.display='none';
        var contraseña=document.getElementById('mostrar_contraseña')
        contraseña.style.display='';
        
}
       
let btn = document.getElementById('boton');
let contraseña=document.getElementById('mostrar_contraseña')
let ocultar=document.getElementById('ocultar_contraseña')

btn.addEventListener('click',generadorcontraseña);
contraseña.addEventListener('click',mostrarcontraseña)
ocultar.addEventListener('click',ocultarcontraseña)
});