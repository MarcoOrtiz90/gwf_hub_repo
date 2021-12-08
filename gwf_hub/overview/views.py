from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.


def overview(response):
    if response.user.is_authenticated:
        context = {
            "overview": True
        }
        return render(response, "overview.html", context)
    else:
        return redirect('login')

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
