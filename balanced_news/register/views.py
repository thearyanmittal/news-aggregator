from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as user_logout
from django.contrib.auth.models import User


def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)

            return redirect('/news')

    else:
        form = RegisterForm()


    return render(request, 'register/register.html', context={"form": form})

def logout(request):
    return render(request, 'home.html', context={"loggedout": True,})

def deleteacct(request):

    if request.user.is_authenticated:
        request.user.delete()
        user_logout(request)
        return render(request, 'home.html', context={"deleted": True,})

    else:
        return redirect('/login')
