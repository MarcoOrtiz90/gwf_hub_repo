from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(response):
    if response.user.is_authenticated:
        context = {
            "overview": True
        }
        return render(response, "overview.html", context)

@login_required
def database(response):
    return render (response, 'database.html', {})

@login_required
def hierarchy(response):
    if response.user.is_authenticated:
        return render(response, "hierarchy.html", {})
    else:
        return redirect('login')
