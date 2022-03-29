from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):    
    # if request.user.is_authenticated:
    return redirect('overview')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('overview')
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
    else:  
        form = AuthenticationForm(request)

    context = {'form': form}
    
    return render(request, "login.html", context)

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, "logout.html", {})

def register_view(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('login')
    context = {'form': form}
    return render(request, "register.html", context)

    # form = UserCreationForm(request.POST or None)
    # if form.is_valid():
    #     user_obj = form.save()
    #     return redirect('login')
    # context = {'form': form}
    # return render(request, "register.html", context)


@login_required
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password was succesfully updated!')
            return redirect('password-change')
        else:
            messages.error(request, 'Please correct below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password-change.html', {'form':form})
    

#@login_required
def profile(request):
    return render(request, "account.html", {})