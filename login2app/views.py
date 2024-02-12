from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.

def home_page(request):
    return render(request,"home_page.html")

def signup_page(request):
    return render(request,"signup_page.html")

def login_page(request):
    return render(request,"login_page.html")

@login_required(login_url='login_page')
def about_page(request):
    if request.user.is_authenticated:
        return render(request, "about_page.html")
    else:
        return HttpResponse("you are not logged in")

def signup(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(username=username).exists():
            messages.info(request, "this username is already exist")
            return redirect("signup_page")
        
        else:
            if password == cpassword:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                print("success")
                return redirect('login_page')
            else:
                messages.info(request, "password is not matching")
                print("password is not matching")
                return redirect ("signup_page")
    
    else:
        return render(request, "signup_page.html")
    
def login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['uid'] = user.id
            messages.info(request, f'welcome {username}')
            return redirect("about_page")
        
        else:
            messages.info(request, "invalid username and password")
            return redirect("login_page")
        
    else:
        return redirect("login_page")

@login_required(login_url='login_page')
def logout(request):
        request.session['uid'] = ""#third method
        auth.logout(request)
        return redirect('home_page')


