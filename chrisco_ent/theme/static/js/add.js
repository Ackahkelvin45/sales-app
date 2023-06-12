   // Function to calculate the total price
   var totalPrice = 0;
   function calculateTotalPrice() {
   
   
  }

  // Event listeners for select and input changes
  $(".search, .quantity").on("change keyup", function() {
    totalPrice = 0
    $(".search").each(function(index) {
      var productId = $(this).val();
      var quantity = $(".quantity").eq(index).val();
      var price = parseFloat($(`option[value="${productId}"]`, this).data("price"));
      console.log($(`option[value="${productId}"]`, this).data("price"))
      if (isNaN(price)){
        price=0
    }
        
      
      
      totalPrice += price * quantity;

     

    });
    $("#total-price").text(totalPrice.toFixed(2));
    $("#total-price-input").val(totalPrice.toFixed(2));
  });


  $("#paid_price").on("keyup", function(){
    paid_price=$(this).val();
  console.log(totalPrice);
  due_value=parseFloat((totalPrice-paid_price).toFixed(2));

  $('#due_amount').text(due_value.toFixed(2));
  $('#due_amount_input').val(due_value.toFixed(2));
   
  })