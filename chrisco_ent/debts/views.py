from django.shortcuts import render,redirect
from  django.urls import reverse
from products.models import Product
from sales.models import Sales
from .forms import DebtForm
from  .models import  Debt
from  django.contrib import  messages
from django.contrib.auth.decorators import login_required
import random
import string

# Create your views here.

@login_required(login_url='auth:login')  
def add_debtpage(request):
  try:
   context={
      "products": Product.objects.all(),
      'sales':Sales.objects.all(),
      "debtform":DebtForm}
   


   return render(request,'debts/add-debt.html',context)
  except:
     return redirect(reverse("/"))


@login_required(login_url='auth:login')  
def add_debt_process(request):
   try:
    if request.method == 'POST':
        debtform=DebtForm(request.POST)
        if  debtform.is_valid():
            debt=debtform.save()
            total_price=request.POST['total_price']
            paid_price=request.POST['paid_price']
            due_amount=request.POST['due_amount']
            serial_number=request.POST['serial_number']
            if Sales.objects.filter(serial_number=serial_number).exists():
              sale=Sales.objects.get(serial_number=serial_number)
              debt.sale=sale
            debt.total_price=total_price
            debt.paid_price=paid_price
            debt.due_price=due_amount
            if int(due_amount) > 0:
               debt.paid='True'
            debt.paid='False'
            debt.save()
            length = 10
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            serial_number = ''.join(random.choices(chars, k=length))
            debt.serial_number = serial_number
            debt.save()
            user=request.user
            debt.created_by=user
            debt.save()
            messages.success(request,"Debt  added successfully")
            return  redirect(reverse('debt:all-debt'))
            
            
        messages.error(request,"Try again,Enter Valid  Data")
        return  redirect(reverse('debt:all-debt'))
   except:
      messages.error(request,"Try again,Sales already have a debt")
      debt.delete()
      return  redirect(reverse('debt:all-debt'))
      
   

          



    
@login_required(login_url='auth:login')          
def all_debtspage(request):
    try:
      context={
         "debts":Debt.objects.all(),
      }

      return render(request,'debts/alldebt.html',context)
    except:
       return redirect(reverse("/"))


def  debt_details(request,pk):
   try:
      debt=Debt.objects.get(id=pk)
      context={
         "debt":debt
      }
      return   render(request,"debts/debt-detailpage.html",context)
   except :
      return redirect(reverse("/"))
@login_required(login_url='auth:login')  
def  edit_debt_page(request,pk):
   try:
      debt=Debt.objects.get(id=pk)
      context={
      "products": Product.objects.all(),
      'sales':Sales.objects.all(),
      "debtform":DebtForm(instance=debt),
      'edit':True,
      'debt':debt
      }
   


      return render(request,'debts/add-debt.html',context)
   except :
      return redirect(reverse("/"))

@login_required(login_url='auth:login')  
def  edit_debt_process(request,pk):
    try:
      if request.method == 'POST':
         debt=Debt.objects.get(id=pk)
         debtform=DebtForm(request.POST,instance=debt)
         if  debtform.is_valid():
               debt=debtform.save()
               total_price=request.POST['total_price']
               paid_price=request.POST['paid_price']
               due_amount=request.POST['due_amount']
               serial_number=request.POST['serial_number']
               if Sales.objects.filter(serial_number=serial_number).exists():
                  sale=Sales.objects.get(serial_number=serial_number)
                  debt.sale=sale
               debt.total_price=total_price
               debt.paid_price=paid_price
               debt.due_price=due_amount
               if int(due_amount) > 0:
                  debt.paid='True'
               debt.paid='False'
               debt.save()
               
               user=request.user
               debt.created_by=user
               debt.save()
               messages.success(request,"Debt  edited successfully")
               return  redirect(reverse('debt:all-debt'))
               
               
         messages.error(request,"Try again,Enter Valid  Data")
         return  redirect(reverse('debt:all-debt'))
    except:
      messages.error(request,"Try again,Sales already have a debt")
      debt.delete()
      return  redirect(reverse('debt:all-debt'))
      
@login_required(login_url='auth:login')  
def delete_debt(request,pk):
   try:
      debt=Debt.objects.get(pk=pk)
      debt.delete()
      messages.success(request,"Debt deleted successfully")
      return  redirect(reverse('debt:all-debt'))
   except:
      messages.error(request,"Try again")
      
      return  redirect(reverse('debt:all-debt'))

