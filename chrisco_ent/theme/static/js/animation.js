const observer5=new IntersectionObserver((e)=>{
    e.forEach((e,i)=>{
        if (e.isIntersecting){
            e.target.classList.add('animate');
         
    
        }
    
      
    })
    
    
    
    })
    const divs=document.querySelectorAll('.divs');

    divs.forEach((element)=>observer5.observe(element));
  
    