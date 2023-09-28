from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib.auth.models import auth, User


# Create your views here.
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        return render(request, 'studentslogin/login.html', {"form": form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            admission = form.cleaned_data['admission number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission, password=password)
            if user:
                login(request, user)
                return redirect("/")

        return render(request, 'studentslogin/login.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('login')