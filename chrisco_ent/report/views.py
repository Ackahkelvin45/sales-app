from django.shortcuts import render
from inventory.models import Iventory
from sales.models import Sales
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='auth:login')  
def inventoryreportpage(request):
      
    
            if  Iventory.objects.count() <= 0:
                
                productIventory=None
                inventory=None
            else:
                productIventory=Iventory.objects.latest("created",'id').products.all()
                inventory=Iventory.objects.latest("created",'id')
            context={
                "productsInventory":productIventory,
                "inventory":inventory,

            }
            return render(request,'report/inventoryreport.html',context)
      
             
        

@login_required(login_url='auth:login')  
def businessIventorypage(request):
    dialysales=Sales.objects.filter(created_date__date=date.today())
    totaldailysaleprice=0
    totaldailysalequantity=0
    
    for  sale in dialysales:
        totaldailysaleprice+=sale.total_price
        totaldailysalequantity+=sale.total_quantity
    context={
         'salesdailydata':Sales.objects.filter(created_date__date=date.today()),
         "totaldailysalequantity":totaldailysalequantity,
         "totaldailysaleprice":totaldailysaleprice,

    }

    return  render(request,'report/businessreport.html',context)