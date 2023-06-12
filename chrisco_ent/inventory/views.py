from django.shortcuts import render,redirect
from django.urls import reverse
from products.models import Product
from.models import Iventory
from .forms import ProductItemForm,IventoryForm
from products.models  import ProductItem,Product
from django.contrib import messages
import random
import string
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="auth:login")
def  addinventorypage(request):
    try:
        context={
            "products": Product.objects.all(),
            "InventoryForm":IventoryForm,
            "ProductItemForm":ProductItemForm
        }

        return render(request, 'inventory/add-inventory.html',context)
    except :
         return redirect(reverse("/"))

@login_required(login_url="auth:login")
def addInventoryprocess(request):
     try:
   
        if request.method == "POST":
            products=Product.objects.all()
            inventoryform=IventoryForm(request.POST)
            if  inventoryform.is_valid():
                inventory=inventoryform.save()
                total_price=0
                total_quantity=0
                for product in products:
                    product=request.POST[product.name]
                    product=Product.objects.get(id=product)
                    quantity=request.POST["quantity"+product.name]
                    productitem=ProductItem.objects.create(total_price=int(product.price.price)*int(quantity),quantity=(quantity))
                    productitem.product=product
                    productitem.save()
                    productitem.save2()
                    inventory.products.add(productitem)
                    total_price+=productitem.total_price
                    total_quantity+=int(quantity)
                    inventory.total_cost=total_price
                    inventory.total_quantity=total_quantity
                    inventory.save()
                length = 10
                chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                serial_number = ''.join(random.choices(chars, k=length))
                inventory.serial_number = serial_number
                inventory.save()
                inventory.save2()
                messages.success(request,"Inventory added successfully")


                return redirect(reverse('inventory:all-inventory')) 
            messages.error(request,"Enter valid data")
            return redirect(reverse('inventory:add-inventory'))
     except :
         messages.error(request,"Error ,Try Again ")
         return redirect(reverse('inventory:add-inventory'))


@login_required(login_url="auth:login")
def editinventory(request,pk):
      inventory=Iventory.objects.get(pk=pk)
      inventoryform=IventoryForm(instance=inventory)
      context={
        "products": Product.objects.all(),
        'inventory': inventory,
        "InventoryForm":inventoryform,
        "edit":True,
      }
      return render(request, 'inventory/add-inventory.html',context)


@login_required(login_url="auth:login")
def editinventory_process(request,pk):
     if request.method == 'POST':
            products=Product.objects.all()
            inventory=Iventory.objects.get(id=pk)
            inventoryform=IventoryForm(request.POST,instance=inventory)
            if  inventoryform.is_valid():
                inventory=inventoryform.save()
                for productitem in  inventory.products.all():
                    inventory.products.remove(productitem)
                    productitem.delete()
                total_price=0
                total_quantity=0
                for product in products:
                    product=request.POST[product.name]
                    product=Product.objects.get(id=product)
                    quantity=request.POST["quantity"+product.name]

                    
                    productitem=ProductItem.objects.create(total_price=int(product.price.price)*int(quantity),quantity=(quantity))
                    productitem.product=product
                    productitem.save()
                    productitem.save2()
                    inventory.products.add(productitem)
                    total_price+=productitem.total_price
                    total_quantity+=int(quantity)
                    inventory.total_cost=total_price
                    inventory.total_quantity=total_quantity
                    inventory.save()
                inventory.save2()
                
                messages.success(request,"Inventory editted successfully")


                return redirect(reverse('inventory:all-inventory')) 
            messages.error(request,"Enter valid data")
            return redirect(reverse('inventory:add-inventory'))



@login_required(login_url="auth:login")
def  inventory_detail(request, pk):
     inventory=Iventory.objects.get(id=pk)
     context={
          "inventory": inventory,
     }

     return render(request,'inventory/inventory-detailpage.html', context)

        
    
      



            


        





@login_required(login_url='auth:login')  
def allinventorypage(request):
    context={
        "inventory":Iventory.objects.all(),
    }
    return render(request, 'inventory/all-inventory.html',context)

@login_required(login_url='auth:login')  
def deleteinventoryprocess(request,pk):
    try:
        inventory=Iventory.objects.get(pk=pk)
        inventory.delete()
        messages.success(request, "inventory deleted successfully")
        return redirect(reverse("inventory:all-inventory"))
    except :
        messages.error(request,"error deleting inventory ")
        return redirect(reverse("inventory:all-inventory"))