from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

def register(request):
    if request.method == "POST":
        messages.debug(request, 'SQL statements were executed.')
        return redirect("register")
    else:
        return render(request,'pages/register.html')

def login(request):
    return render(request, 'pages/login.html')

def logout(request):
        return redirect('index')

def dashboard(request):
    return render(request, 'pages/dashboard.html')