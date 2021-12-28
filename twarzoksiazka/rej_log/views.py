from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import  CreateUserDetailsForm, CreateUserForm
from .models import User_details, User
from django.contrib.auth.hashers import make_password


def register(request):
    form1 = CreateUserForm(request.POST)
    form2 = CreateUserDetailsForm(request.POST)
   


   
    if form1.is_valid():

        email = form1.cleaned_data.get("email")
        user=  User(username = request.POST['email'], email = request.POST['email'], password = make_password( request.POST['password1'] ))
        user.save()

       




        
       
    context={
        'form1':form1,
        'form2':form2
      

    }

    return render(request,"register.html",context)



def viev_login(request):

    
    context={
     
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(hello_login)
        else:
            messages.info(request,'Username or password is incorrect')
            return  render(request,"login.html",context)
  



    return  render(request,"login.html",context)

def hello_login(request):
    return render(request,"hello.html",{} )



