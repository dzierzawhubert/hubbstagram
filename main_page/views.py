from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'Post': Post.objects.all()
    }
    return render(request, 'main_page/home.html', context)

