from django.shortcuts import render, redirect
from .forms import UsersProfile, UserRegisterForm, CreatePost, UserUpdate
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

 @login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form1 = UserUpdate(request.POST,instance=request.user)
        form2 = UsersProfile(request.POST, instance=request.user.usersprofile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('profile')
    else:
        form1 = UserUpdate(instance=request.user)
        form2 = UsersProfile(instance=request.user.usersprofile)

    context = {
        'form1' : form1,
        'form2' : form2
    }

    return render(request, 'users/profile_update.html', context)

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
