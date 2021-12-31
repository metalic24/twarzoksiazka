from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render



from .forms import  CreateUserDetailsForm, CreateUserForm, UpdateUserDetailsForm, User_details
from .models import Relationship, User_details, User
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.postgres.search import SearchVector



def register(request):
    form1 = CreateUserForm(request.POST)
    form2 = CreateUserDetailsForm(request.POST)
   

  
   
    if form1.is_valid() and form2.is_valid():

        email = form1.cleaned_data.get("email")
        user=  User(username = request.POST['email'], email = request.POST['email'], password = make_password( request.POST['password1'] ))
        user.save()

        birth_date = request.POST['birth_date_year'] +'-' + request.POST['birth_date_month'] +'-'  + request.POST['birth_date_day']
        
        user_details = User_details(user = user, name = request.POST['name'], surr_name = request.POST['surr_name'],
        birth_date = birth_date , bio = request.POST['bio'] 
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

def log_out(request):
    logout(request)
    return redirect(viev_login)

#user profile viev
def hello_login(request):

    obj = User_details.objects.get(user = request.user)
    context = {
        'obj': obj
    }




    return render(request,"hello.html",context )

def update_user_details(request):
    obj = User_details.objects.get(user = request.user)
    form = UpdateUserDetailsForm( request.POST or None, request.FILES or None ,instance=obj )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = User.objects.get(id = request.user.id)
            user.first_name = request.POST['name']
            user.last_name = request.POST['surr_name']
            user.save()

    context={

        'obj':obj,
        'form':form
    }

    return render(request,"update.html",context )

def get_profiles(request):
        obj = User_details.objects.get(user = request.user)
        query = request.GET.get('query')
        now_u = User_details.objects.all()
       
        profile_list = User_details.objects.filter(
            Q(name__icontains = query) | Q(surr_name__icontains = query)
        ).exclude(user= request.user)
      
        context = {
            'profile_list': profile_list,
            'now_u': now_u,
        }
        return render(request, 'search.html', context)



def show_infitations(request):
     reciver = User_details.objects.get(user = request.user)
     
     rels = Relationship.objects.filter(reciver=reciver, status='send')

     senders=[]
    

     for rel in rels:
         sender = User_details.objects.get(user = rel.sender.user)
         
         senders.append(sender)
         
         
     invites = zip(senders,rels)
    

     context ={
         'invites':invites
    }
     return render(request, 'invitations.html', context)





def add_friend(request):
    if request.method == "POST":
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = User_details.objects.get(user=user)
        reciver = User_details.objects.get(pk=pk)

        rel = Relationship.objects.filter( (Q(sender = sender) & Q(reciver = reciver)) | (Q(sender = reciver) & Q(reciver = sender)) )

        print(rel)
        if not rel:

             relation = Relationship.objects.create(sender = sender, reciver = reciver, status = 'send')
        

        
        return redirect(hello_login)

    return redirect("viev_login")

def accept_invite(request):
     if request.method == "POST":
        pk = request.POST.get('invite_pk')
        invite = Relationship.objects.get(pk=pk)

        invite.status= 'accepted'
        invite.save()
     return redirect(hello_login)




    