from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'Home/index.html',{
            'name':request.user.get_full_name()
        })
    else:
        return redirect(signup)

def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                if User.objects.filter(username=username).exists():
                    return HttpResponse('Username is already exists')
                elif User.objects.filter(email=email).exists():
                    return HttpResponse('Email is already Exists')
                else:
                    try:
                        user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                        user.save()
                        return HttpResponse('User Create Successfully')
                    except:
                        return HttpResponse('Error')
            else:
                return HttpResponse('Password do not match')
    else:
            return render(request,'Userauthor/register.html')
         
    
   

# return render(request,'Userauthor/login.html')
def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            return HttpResponse('Login Failed! Wrong username or password')

    
    return render(request,'Userauthor/login.html')
    

def signout(request):
    logout(request)
    return redirect(home)

def profile(request):
    if request.user.is_authenticated:
        return render(request,'Userauthor/profile.html',{
            'name':request.user.get_full_name(),
            'email':request.user.email
        })
    else:
        return redirect(signin)
    

def editinfo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            user = request.user
            if firstname is not None or firstname !='':
                user.first_name = firstname
            if lastname is not None or lastname !='':
                user.last_name = lastname
            if email is not None or email !='':
                if User.objects.filter(email=email).exists():
                    return HttpResponse('Email is already Exists')
                else:
                    user.email = email
            user.save()
            return HttpResponse('Update Successfully')
        else:
            return render(request,'Userauthor/editinfo.html',{
                'firstname':request.user.first_name,
                'lastname':request.user.last_name,
                'email':request.user.email
            })
    else:
        return redirect(home)

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            oldpassword = request.POST.get('oldpassword')
            newpassword = request.POST.get('newpassword')
            newpassword2 = request.POST.get('newpassword2')
            user = request.user
            if user.check_password(oldpassword):
                if newpassword == newpassword2:
                    user.set_password(newpassword)
                    user.save()
                    return HttpResponse('Change Password Successfully')
                else:
                    return HttpResponse('New Password is not Same')
            else:
                return HttpResponse('Old password is incorrct')
        else:
            return render(request,'Userauthor/changepassword.html')

    else:
        return redirect(home)