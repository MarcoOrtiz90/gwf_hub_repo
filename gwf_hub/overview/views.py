from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

##@login_required
def overview(response):
    context = {'main': "main"}
    return render(response, 'applications.html', context)

def database(response):
    if response.user.is_authenticated:
        return render (response, 'database.html', {})
    else:
        return redirect('login')

def hierarchy(response):
    if response.user.is_authenticated:
        return render(response, "hierarchy.html", {})
    else:
        return redirect('login')

