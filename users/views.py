from django.shortcuts import render, redirect
from .forms import UsersProfile, UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcom to Hubbstagram, {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})

def profile(request):
    context = {
        'form' :  UsersProfile()
    }
    return render(request, 'users/profile.html', context)

def login(request):
    context = {
        'form' :  UsersProfile()
    }
    return render(request, 'users/login.html', context)
