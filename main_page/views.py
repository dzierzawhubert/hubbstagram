from django.shortcuts import render
from .models import Post
from users.models import CreatePost

def home(request):
    context = {
        #'Post'
        'posts': CreatePost.objects.all()
    }
    return render(request, 'main_page/home.html', context)

