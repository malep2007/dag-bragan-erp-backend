from django.shortcuts import render, reverse, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, "index.html", { "title": "Home"})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request,user)
                return redirect('customer:index')
            else:
                form = LoginForm()
                return render(request, 'login.html', {
                    "form": form,
                    "title": "Login",
                    "user": None
                })
            # return reverse('customer:index')
    else:
        form = LoginForm()
    return render(request, "login.html", {
        "form": form,
        "title": "Login",
        "user": None
    })
