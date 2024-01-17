from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import District,Customer,Branch,Login


# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('bankapp:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('bankapp:login')

        else:
            messages.info(request, "password does not match")
            return redirect('bankapp:register')
        return redirect('/')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:formpage')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('bankapp:login')
    return render(request, "login.html")
def formpage(request):
    if request.method == 'POST':
        messages.info(request, "Form Submitted Successfully")
        # return redirect('bankapp:formpage.html')
    return render(request,'formpage.html')

def getDistrict(request):
    district=District.objects.all()
    branch=Branch.objects.all()
    return render(request,'formpage.html',{'district':district,'branch':branch})
def logout(request):
    auth.logout(request)
    return redirect('/')