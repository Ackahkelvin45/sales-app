from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from products.models import Product
from inventory.models import Iventory
from .forms import SalesForm
from django.contrib.auth.decorators import login_required
from products.models import ProductItem
from .models import Sales
from django.contrib import messages
import random
import string
from django.http import FileResponse,Http404
from docxtpl import DocxTemplate
from datetime import date,timezone,datetime
from django.db.models import Sum
from debts.models import Debt
from inventory.forms import ProductItemForm,IventoryForm
from products.models  import ProductItem,Product


# Create your views here.


@login_required(login_url="auth:login")
def index(request):
    try:
        context={
            "products":Product.objects.count(),
            'inventory':Iventory.objects.count(),
            'productsInventory':Iventory.objects.latest("created",'id').products.all(),
            'salesdailydata':Sales.objects.filter(created_date__date=date.today()),
        
            

        }

        return render(request,"sales/index.html",context)
    except:
        context={
            "products":Product.objects.count(),
            'inventory':Iventory.objects.count(),
            'productsInventory':None,
            'salesdailydata':Sales.objects.filter(created_date__date=date.today()),
        
            

        }

        return render(request,"sales/index.html",context)


@login_required(login_url="auth:login")
def addsalespage(request):
    context={
        "products":Product.objects.all(),
        "salesform":SalesForm
    }

    return render(request,"sales/addsales.html",context)

@login_required(login_url="auth:login")
def allsalespage(request):
    context={
        "sales":Sales.objects.all( )
    }
    return render(request,"sales/allsales.html",context)

@login_required(login_url="auth:login")
def  addsalesprocess(request):
    if Iventory.objects.count()>0   :
 
        if request.method == "POST":
            products=Product.objects.all()
            salesform=SalesForm(request.POST)
            if  salesform.is_valid():
                sales=salesform.save()
                sales.inventory=Iventory.objects.latest('created','id') 
                sales.save()
                total_price=0
                due_amount=0
                total_price=request.POST["total_price"]
                due_amount=request.POST["due_amount"]
                total_quantity=0    
                for product in products:
                        product=request.POST[product.name]
                        
                        if Product.objects.filter(id=product).exists():
                            product=Product.objects.get(id=product)

                            quantity=request.POST["quantity"+product.name]
                            productitem=ProductItem.objects.create(total_price=int(product.price.price)*int(quantity),quantity=(quantity))
                            productitem.product=(product)
                            productitem.save()
                            sales.products.add(productitem)
                    
                            total_quantity+=int(quantity)
                            sales.save()
                    
                newinventorycost=sales.inventory.new_total_cost
                newinventoryquantity=sales.inventory.new_total_quantity
                for saleproduct  in sales.products.all():
                    for inventoryproduct in sales.inventory.products.all():
                        if saleproduct.product ==  inventoryproduct.product:
                                if inventoryproduct.new_quantity >0:
                        
                                    inventoryproduct.new_quantity = inventoryproduct.new_quantity-saleproduct.quantity
                                    inventoryproduct.new_total_price = inventoryproduct.new_total_price - saleproduct.total_price
                                    inventoryproduct.save()
                                    newinventorycost +=saleproduct.total_price
                                    newinventoryquantity +=saleproduct.quantity
                                    sales.inventory.new_total_cost=sales.inventory.new_total_cost - saleproduct.total_price
                                    sales.inventory.new_total_quantity=sales.inventory.new_total_quantity-saleproduct.quantity
                                else:
                                    sales.delete()
                                    messages.error(request, inventoryproduct.product.name+" out of stock")
                                    return redirect(reverse('sales:add-sales'))
                    
                                
                    
                            
                
                    
                        

            
                sales.inventory.save()       
                sales.total_price=total_price
                sales.due_price=due_amount
                sales.total_quantity=total_quantity 
                sales.created_by=request.user
                
                if float(sales.due_price) <= 0:
                    sales.debt="False"
                else:
                    sales.debt="True"

                length = 10
                chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                serial_number = ''.join(random.choices(chars, k=length))
                sales.serial_number = serial_number
                sales.save()

                
                length = 10
                chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                serial_number2 = ''.join(random.choices(chars, k=length))
                debt=Debt.objects.create(serial_number=serial_number2, total_price=total_price,due_price=due_amount, created_by=request.user,sale=sales,paid_price=sales.paid_price)
                if float(debt.due_price )> 0:
                    debt.paid='False'
                    debt.paid='True'
                    debt.customer_name =sales.customer_name
                    debt.save()
                    messages.success(request,'sale added successfully')
                    return redirect(reverse('sales:all-sales'))
            messages.error(request,'provide  valid  data ')
            return redirect(reverse('sales:add-sales'))
    else:
        messages.error(request,'add Inventory first')
        return redirect(reverse('sales:add-sales'))
        

      
    
            
                
@login_required(login_url="auth:login")
def  salesdetailpage(request,pk):

    sale=Sales.objects.get(id=pk)
    context={
        "sale": sale
    }

    return render(request,"sales/salespagedetail.html",context)

@login_required(login_url="auth:login")
def download_sale(request,pk):
 try:
    sale=Sales.objects.get(id=pk)
    doc = DocxTemplate("sales_detail.docx")
    context = {
            'sale':sale,
            'products':sale.products.all(),
            'date_created':sale.created_date.strftime("%Y-%m-%d"),
            'timestamp': sale.created_date.strftime("%H:%M:%S")
            }
        
    doc.render(context)
    doc.save("sale_details.docx")
    return FileResponse(open("sale_details.docx", 'rb'), content_type='application/docx')
 except :
     return Http404


def delete_sale(request, pk):

    try:
        sale=Sales.objects.get(pk=pk)
        sale.delete()
        messages.success(request,'Sales deleted successfully')
        return redirect(reverse('sales:all-sales'))
    except:
        messages.error(request,"error deleting ,try again")
        return redirect(reverse('sales:all-sales'))

@login_required(login_url="auth:login")
def edit_sales(request,pk):
    sale=Sales.objects.get(id=pk)
    saleform=SalesForm(instance=sale)

    context={
        "salesform":saleform,
        "edit":True,
        'sale':sale,
        "products":Product.objects.all(),
        
    }

    return render(request,"sales/addsales.html",context)

@login_required(login_url="auth:login")
def edit_sales_process(request,pk):
   
    if request.method == "POST":
        products=Product.objects.all()
        sale=Sales.objects.get(pk=pk)
        if Debt.objects.filter(sale_id=sale.id).exists():
            debt=Debt.objects.get(sale_id=sale.id)
            debt.delete()
        salesform=SalesForm(request.POST,instance=sale)
        if  salesform.is_valid():
            sales=salesform.save()
            
            total_price=0
            due_amount=0
            total_price=request.POST["total_price"]
            due_amount=request.POST["due_amount"]
            total_quantity=0 

            
            
            
            newinventorycost=sales.inventory.new_total_cost
            newinventoryquantity=sales.inventory.new_total_quantity
            for saleproduct  in sales.products.all():
                for inventoryproduct in sales.inventory.products.all():
                    if saleproduct.product ==  inventoryproduct.product:
                  
                        inventoryproduct.new_quantity = inventoryproduct.new_quantity+saleproduct.quantity
                        inventoryproduct.new_total_price = inventoryproduct.new_total_price +saleproduct.total_price
                        inventoryproduct.save()
                        newinventorycost +=saleproduct.total_price
                        newinventoryquantity +=saleproduct.quantity
                        sales.inventory.new_total_cost=sales.inventory.new_total_cost +saleproduct.total_price
                        sales.inventory.new_total_quantity=sales.inventory.new_total_quantity+saleproduct.quantity
                        sales.inventory.save()

            for item in  sales.products.all():
              sales.products.remove(item)
              item.delete()
            sales.save()  
            for product in products:
                    product=request.POST[product.name]
                    
                    if Product.objects.filter(id=product).exists():
                        product=Product.objects.get(id=product)

                        quantity=request.POST["quantity"+product.name]
                        productitem=ProductItem.objects.create(total_price=int(product.price.price)*int(quantity),quantity=int(quantity))
                        productitem.product=(product)
                        productitem.save()
                        sales.products.add(productitem)
                        sales.save()
                
                        total_quantity+=int(quantity)
                        sales.total_quantity=total_quantity
                        sales.save()
                   
            newinventorycost=sales.inventory.new_total_cost
            newinventoryquantity=sales.inventory.new_total_quantity
            for saleproduct  in sales.products.all():
                for inventoryproduct in sales.inventory.products.all():
                    if saleproduct.product ==  inventoryproduct.product:
                  
                        inventoryproduct.new_quantity = inventoryproduct.new_quantity-saleproduct.quantity
                        inventoryproduct.new_total_price = inventoryproduct.new_total_price - saleproduct.total_price
                        inventoryproduct.save()
                        newinventorycost +=saleproduct.total_price
                        newinventoryquantity +=saleproduct.quantity
                        sales.inventory.new_total_cost=sales.inventory.new_total_cost - saleproduct.total_price
                        sales.inventory.new_total_quantity=sales.inventory.new_total_quantity-saleproduct.quantity
                        
            
                
                    

           
            sales.inventory.save()       
            sales.total_price=total_price
            sales.due_price=due_amount
            
            
            if float(sales.due_price) <= 0:
                sales.debt="False"
            else:
                sales.debt="True"

            
            sales.save()
            length = 10
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            serial_number2 = ''.join(random.choices(chars, k=length))
            debt=Debt.objects.create(serial_number=serial_number2, total_price=total_price,due_price=due_amount, created_by=request.user,sale=sales,paid_price=sales.paid_price)
            if float(debt.due_price )> 0:
                    debt.paid='False'
                    debt.paid='True'
                    debt.customer_name =sales.customer_name
                    debt.save()
            messages.success(request,'sale edited successfully')
            return redirect(reverse('sales:all-sales'))
        messages.error(request,' error please try again')
        return redirect(reverse('sales:add-sales'))
