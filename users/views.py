from django.shortcuts import render, redirect
from .forms import UsersProfile, UserRegisterForm, CreatePost
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    return render(request, 'users/profile.html')

def profile_update(request):
    if request.method == 'POST':
        form = UsersProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UsersProfile()

    return render(request, 'users/profile_update.html', {'form' : form})

def login(request):
    context = {
        'form' :  UsersProfile()
    }
    return render(request, 'users/login.html', context)

@login_required
def create_post(request):
    context = {
        'form' : CreatePost()
    }
    return render(request, 'users/create_post.html', context)
