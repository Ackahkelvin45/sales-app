document.getElementById("profile-icon").addEventListener("click",(event)=>{

    document.getElementById("profile-icon").style.border=" 4px  solid rgba(124 ,45, 18,0.2)";

    event.stopPropagation(); 

    
    document.getElementById("profile-dropdown").style.display    = document.getElementById("profile-dropdown").style.display === 'flex' ? 'none' : 'flex';

   
   
});

document.addEventListener("click",(function() {
    document.getElementById("profile-dropdown").style.display="none";
    document.getElementById("profile-icon").style.border="";
  }));



document.getElementById("sales").addEventListener("click", ()=>{
    if (document.getElementById("arrow-1").style.transform !=="rotate(90deg)"){
    document.getElementById("arrow-1").style.transform="rotate(90deg)"
   

    document.getElementById("sub-sales").style.display = "flex";
    }
    else{
        document.getElementById("arrow-1").style.transform="rotate(0deg)"
        document.getElementById("sub-sales").style.display = "none";
      
    }


});

document.getElementById("debt").addEventListener("click", ()=>{
    if (document.getElementById("arrow-2").style.transform !=="rotate(90deg)"){
    document.getElementById("arrow-2").style.transform="rotate(90deg)"
   

    document.getElementById("sub-debt").style.display = "flex";
    }
    else{
        document.getElementById("arrow-2").style.transform="rotate(0deg)"
        document.getElementById("sub-debt").style.display = "none";
      
    }


});


document.getElementById("inventory").addEventListener("click", ()=>{
    if (document.getElementById("arrow-3").style.transform !=="rotate(90deg)"){
    document.getElementById("arrow-3").style.transform="rotate(90deg)"
   

    document.getElementById("sub-inventory").style.display = "flex";
    }
    else{
        document.getElementById("arrow-3").style.transform="rotate(0deg)"
        document.getElementById("sub-inventory").style.display = "none";
      
    }


});


document.getElementById("products").addEventListener("click", ()=>{
    if (document.getElementById("arrow-4").style.transform !=="rotate(90deg)"){
    document.getElementById("arrow-4").style.transform="rotate(90deg)"
   

    document.getElementById("sub-products").style.display = "flex";
    }
    else{
        document.getElementById("arrow-4").style.transform="rotate(0deg)"
        document.getElementById("sub-products").style.display = "none";
      
    }


});













document.getElementById("report").addEventListener("click", ()=>{
    if (document.getElementById("arrow-5").style.transform !=="rotate(90deg)"){
    document.getElementById("arrow-5").style.transform="rotate(90deg)"
   

    document.getElementById("sub-report").style.display = "flex";
    }
    else{
        document.getElementById("arrow-5").style.transform="rotate(0deg)"
        document.getElementById("sub-report").style.display = "none";
      
    }


});







document.getElementById("nav-bar").addEventListener("click",()=>{

if (document.getElementById("side-bar").style.transform =="translateX(-100%)"){
    document.getElementById("side-bar").style.transform="translateX(0px)"
   
}
else {
    document.getElementById("side-bar").style.transform ="translateX(-100%)"

}
}
)

document.getElementById("nav-bar-1").addEventListener("click",()=>{

    if (document.getElementById("side-bar").style.transform =="translateX(-100%)"){
        document.getElementById("side-bar").style.transform="translateX(0px)"
        console.log(document.getElementById("side-bar").style.transform)
        if (window.screen.width>1057){
            document.getElementById("index-body").style.paddingLeft = "20%"

        }
        else if (window.screen.width>900){
            document.getElementById("index-body").style.paddingLeft = "25%"
        }
        else if(window.screen.width>768){
            document.getElementById("index-body").style.paddingLeft = "28%"

        }
        else if(window.screen.width>640){
            document.getElementById("index-body").style.paddingLeft = "33%"

        }


    }
    else {
        document.getElementById("side-bar").style.transform ="translateX(-100%)"
        document.getElementById("index-body").style.paddingLeft = "0px"
   
    
    }
    }
    )

    