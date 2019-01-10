from django.shortcuts import render, reverse, HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, "index.html", { "title": "Home"})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                return HttpResponse("valid user")
            # return reverse('customer:index')
    else:
        form = LoginForm()
    return render(request, "login.html", {
        "form": form,
        "title": "Login"
    })
