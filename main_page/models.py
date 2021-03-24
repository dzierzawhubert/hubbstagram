from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to = 'main_page/images')
    description = models.TextField(max_length=400)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Posted by:{self.author}, descritption:{self.description}'
