from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
import re
from .forms import SignUpForm 
from .models import CustomUserManager

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password', '')
        
        if email and password:
            user = authenticate(email=email, password=password)
            
            if user is not None:
                auth_login(request, user)
                
            print(user)
            print(request.user.is_authenticated)
    return render(request, 'account/login.html')
    
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm()
        if form.is_valid():
            user = CustomUserManager()
            user.username = form.cleaned_data.get('username')
            user.name = form.cleaned_data.get('name')
            user.email = form.cleaned_data.get('email') 
            user.phone = form.cleaned_data.get('phone')
            print(user)
            user.save()
            return redirect('login')
        else:
            print('Form is invalid')
    else:
        print('GET request')
    return render(request, 'account/signup.html')