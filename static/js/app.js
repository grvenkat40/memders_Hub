const msg = document.getElementById('messages')
if (msg){
    setTimeout(() =>{
        msg.style.opacity = '0';
        msg.style.transition = "opacity 0.3s eaase";

    setTimeout(() =>{
        msg.style.display = "none";
    }, 500);
    }, 3000);
}