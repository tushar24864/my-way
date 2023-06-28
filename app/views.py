
from django.shortcuts import render, redirect
from django. contrib.auth.models import User, auth
from django.contrib import messages
from app.models import confidential

# Create your views here.
def home(request):
    confidential_data= confidential.objects.all()

    data = {
        'confidential_data':confidential_data
    }

    return render(request, "home.html",data)
def register(request):   
    if request.method=='POST':
        first_name= request.POST['first_name'] 
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect("register")
            else:
                user= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                
                user.save()
                print("success")
                return redirect('login')
    else:
        print("this is not POST method")
    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
           auth.login(request ,user)
           return redirect('home')
        else:   
          messages.info(request, 'Invalid username or Password')
        return redirect('login')
    else: 
      return render(request,"login.html")
    
def logout(request):
        auth.logout(request)
        return redirect('home')