from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email ')
            password = form.cleaned_data.get('password1 ')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('home')
    return render(request, 'register.html')