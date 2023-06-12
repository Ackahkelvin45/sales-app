document.getElementById("logout").addEventListener("click", (e)=>{

    Swal.fire({
        icon: 'warning',
        text: "Are you sure?",
        title:"logout",
        showConfirmButton:true,
        showCancelButton:true,
        confirmButtonColor: '#4ade80',
        confirmButtonText:"Yes",
        color:"white",
        background: 'rgba(0, 0, 0, 0.7)',
        allowEscapeKey: false,

       
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
           
            log=e.target.getAttribute("data-url")

            window.location.href=log
        } else if (result.isDenied) {
         
        }
      })
      
    })