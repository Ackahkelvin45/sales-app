from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from  .forms import ProductForm,PriceForm
from  .models import Product,Price
import random
import string
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="auth:login")
def addproductspage(request):
    context={
        "ProductForm":ProductForm,
        "PriceForm":PriceForm,
    }

    return render(request,"products/addproducts.html", context)


@login_required(login_url="auth:login")
def addproductprocess(request):
  try:
     if request.method=="POST":
        Productform=ProductForm(request.POST)
        Priceform=PriceForm(request.POST)
        if Productform.is_valid() and Priceform.is_valid():
           product=Productform.save()
           price=Priceform.save()
           product.price=price
           length = 10
           chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
           serial_number = ''.join(random.choices(chars, k=length))
           product.serial_number = serial_number
           product.save()
           messages.success(request,'Product saved successfully')
           return redirect(reverse('products:all-products'))  
        else:
           messages.error(request,'error trying to save product')
           return redirect(reverse('products:add-products')) 
        
  except Exception as e:
     messages.error(request, 'please Enter valid data')
     return redirect(reverse('products:add-products')) 
           


@login_required(login_url="auth:login")
def allproductspage(request):
    products=Product.objects.all()
    context={
       "products": products
    }
    
    return render(request,"products/allproducts.html", context)

@login_required(login_url="auth:login")
def editproductspage(request,pk):
   try:
      product=Product.objects.get(id=pk)
      price=Price.objects.get(id=product.price.id)
      Productform=ProductForm(instance=product)
      Priceform=PriceForm(instance=price)

      context={
         'ProductForm': Productform,
         'PriceForm': Priceform,
         "edit":True,
         "product":product,
      }

      return render(request,"products/addproducts.html", context)
   

   except Exception as e:
    return redirect("/")
   

@login_required(login_url="auth:login")
def deleteproduct(request,pk):
  
      product=Product.objects.get(id=pk)
      product.delete()
      messages.success(request,"Product   deleted successfully")
      return redirect(reverse('products:all-products'))
   

    

@login_required(login_url="auth:login")   
def productdetail(request,pk):
   productdetail=Product.objects.get(id=pk)
   context={
      "product":productdetail
   }

   return render (request, "products/productdetail.html", context)


@login_required(login_url='auth:login')  
def  editproductprocess(request,pk):
  try:    
     if request.method=="POST":
        product=Product.objects.get(pk=pk)
        Productform=ProductForm(request.POST,instance=product)
        Priceform=PriceForm(request.POST,instance=product.price)
        
        if Productform.is_valid() and Priceform.is_valid():
           product=Productform.save()
           price=Priceform.save()
           
           product.price=price
           product.save()
           messages.success(request,'Product edited successfully')
           return redirect(reverse('products:all-products'))  
        else:
           messages.error(request,'error trying to edit product')
           return redirect(reverse('products:add-products')) 
        
  except Exception as e:
     messages.error(request, 'please Enter valid data')
     return redirect(reverse('products:add-products')) 


   