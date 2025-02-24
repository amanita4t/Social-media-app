from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists:
                messages.info(request, 'Email already taken')
                return redirect('signup')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')
