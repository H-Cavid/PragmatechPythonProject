from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from backend.models import User


# Create your views here.
def get_register(request):
    if request.method == 'POST':
        print('method isdiyir?')
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username already taken...')
                messages.info(request,'Username already taken...')
                return redirect("get_register")
            elif User.objects.filter(email=email).exists():
                print('Email already taken ...')
                messages.info(request,'Email already taken...')
                return redirect("get_register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                print("user is created")
                return redirect("get_login")
        else:
            print('Password not maching...')
            messages.info(request,'Password not maching ...')
            return redirect("get_register")

        return redirect("index")
        
    else:
        return render(request,"accounts/register.html")


def get_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            print("invalid credentials")
            return redirect("get_login")
    else:
         return render(request,"accounts/login.html")

def get_logout(request):
    logout(request)
    return redirect("index")