from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import  CreateUserDetailsForm, CreateUserForm
from .models import User_details, User
from django.contrib.auth.hashers import make_password


def register(request):
    form1 = CreateUserForm(request.POST)
    form2 = CreateUserDetailsForm(request.POST)
   

  
   
    if form1.is_valid() and form2.is_valid():

        email = form1.cleaned_data.get("email")
        user=  User(username = request.POST['email'], email = request.POST['email'], password = make_password( request.POST['password1'] ))
        user.save()

        birth_date = request.POST['birth_date_year'] +'-' + request.POST['birth_date_month'] +'-'  + request.POST['birth_date_day']
        
        user_details = User_details(user = user, name = request.POST['name'], surr_name = request.POST['surr_name'],
        birth_date = birth_date , bio = request.POST['bio'] ,profile_img = request.POST['profile_img']
        )

        user_details.save()

        #dodatkowo sobię to dodaję, bo potem to się przyda
        user.first_name = user_details.name
        user.last_name = user_details.surr_name

        user.save()

        login(request,user)
        return redirect(hello_login)
       




        
       
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



