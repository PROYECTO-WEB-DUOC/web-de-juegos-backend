
document.addEventListener('DOMContentLoaded', () => {

let btnblanco=document.getElementById('fondoblanco')
let body=document.getElementById('body')
let btnnegro=document.getElementById('fondonegro')
let navbar=document.getElementById('navbar')
let navlink=document.getElementById('navlink')
let video=document.getElementById('video')
let contador=document.getElementById('contador')
let navbar_toggler=document.getElementById('navbar_toggler');
let titulos=document.getElementById('titulo')
let titulos2=document.getElementById('titulo2')
let titulos3=document.getElementById('titulo3')
let footer=document.getElementById('footer')
let blanco=document.getElementById('blanco')
let negro=document.getElementById('negro')
let next=document.getElementById('next')
let prev=document.getElementById('prev')
btnnegro.addEventListener('click',(e)=>{
    e.preventDefault();
    body.style='background: #fff; '
    navlink.style='color: black'
    contador.style='color:black'
    navbar_toggler.style='border: 1px solid white; background-color:#fff;'
    titulos.style='color:black;'
    titulos2.style='color:black;'
    titulos3.style='color:black;'
    footer.style='--bs-bg-opacity: 0; background: linear-gradient(rgb(40, 40, 40), rgb(56, 56, 56));'
    blanco.style='background-color:#0b5ed7'
    negro.style=''
    next.style='background-color:rgb(56, 56, 56)'
    prev.style='background-color:rgb(56, 56, 56)'
})


btnblanco.addEventListener('click',(e)=>{
    e.preventDefault();
    body.style=''
    navbar.style=''
    navlink.style='color: black'
    video.style=''
    contador.style=''
    navbar_toggler.style=''
    titulos.style=''
    titulos2.style=''
    titulos3.style=''
    footer.style=''
    blanco.style=''
    negro.style='background-color:#0b5ed7'
    next.style=''
    prev.style=''
})

});