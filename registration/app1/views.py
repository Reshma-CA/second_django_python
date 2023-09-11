from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import never_cache

# Create your views here.


@login_required
def HomePage(request):
    return render(request,'home.html',{})


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')


        new_user = User.objects.create_user(name,email,password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request,'register.html',{})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request,username = name,password = password)
        if user is not None:
            login(request,user)
            return redirect('home-page')
        else:
            return HttpResponse("Error, User does not exist")


    return render(request,'login.html',{}) 

def logoutuser(request):
    logout(request)
    return redirect('login-page')























