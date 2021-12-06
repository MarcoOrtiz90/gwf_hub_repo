from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('overview')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password'}
            return render(request, "login.html", context)
        else:
            login(request, user)
            return redirect('overview')

    return render(request, "login.html", {})

def logout(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "login.html", {})