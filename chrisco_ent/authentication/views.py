from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from difflib import SequenceMatcher

# Create your views here.

def loginpage(request):
    return render(request,'authentication/login.html')


def  loginprocess(request):
    try:
        if request.method=='POST':
            username = request.POST['username'].lower()
            password = request.POST['password']
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"logged  in ") 
                return HttpResponseRedirect(reverse("sales:index"))
            messages.error(request,"Invalid Credentials")
            return redirect(reverse("auth:login"))
    except :
         messages.error(request,"Invalid Credentials")
         return redirect(reverse("auth:login"))
        

def logout_process(request):
    try:
        logout(request)
        return redirect(reverse("auth:login"))
    except :
         messages.error(request,"Try again")
         return redirect(reverse("/"))


def signup_page(request):

    return render(request,"authentication/signup.html")

def  add_user_process(request):
 try:
        if request.method == "POST":
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            password=request.POST["password"]
            phone_number=request.POST["phone_number"]
            is_admin=request.POST["is_admin"]
            user=User.objects.create(username=username,first_name=first_name,last_name=last_name,phone_number=phone_number)
            user.set_password(password)
            user.save()
            if is_admin=="True":
                user.is_superuser=True
                user.save()
            messages.success(request,"user added successfully")
            return redirect(reverse("auth:add-user"))
 except:
     messages.error(request,'username  already in use')
     return redirect(reverse("auth:add-user"))

@login_required(login_url='auth:login') 
@user_passes_test(lambda u: u.is_superuser)
def view_users(request):
    try:
        context={
            "users":User.objects.all()


        }

        return render(request, 'authentication/viewusers.html', context)
    except:
        return redirect(reverse("/"))


        
        
@login_required(login_url='auth:login')  
def userpage(request):
 try:
    context={
        'user':request.user
    }

    return render(request, 'authentication/userspage.html', context)
 except:
     return redirect(reverse("/"))

@login_required(login_url='auth:login')  
def  changepasswords(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                user=User.objects.get(username=username)
                new_password = request.POST['new_password']
                
                user.set_password(new_password)
                user.save()
            
                messages.success(request,'Password  changed successfully')
                return redirect('/')
            
        else:
            messages.error(request,'Username does not exist')
            return redirect('/')
    except :
        return redirect(reverse("/"))
@login_required(login_url='auth:login') 
@user_passes_test(lambda u: u.is_superuser)     
def delete_user(request,pk):
    try:
        user=User.objects.get(id=pk)
        user.delete()
        messages.success(request,'User Deleted Successfully')
        return redirect(reverse("auth:view-users"))
    except:
        return redirect(reverse("/"))

@login_required(login_url='auth:login')  
def  view_details(request,pk):
     try:
        context={
            "users":User.objects.all(),
            'view_details':True,
            'user':User.objects.get(pk=pk)


        }

        return render(request, 'authentication/viewusers.html', context)
     except :
         return redirect(reverse("/"))

        
          
          

