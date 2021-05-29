from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UsersProfile(models.Model):

    gender = [ ('M' , 'Male'), ('F' , 'Female'), ('TM', 'Trans Male'), \
        ('TF', 'Trans Female'), ('Q', 'Queer'), ('F', 'Genderfluid'), ('AT', 'Attack Helicopter'), ('D', 'Dog') ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    profile_pic = models.ImageField(default='default.jpg', upload_to='users/')
    name = models.CharField(max_length=50)
    sec_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=120, choices=gender)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name},{self.email},{self.phone_number}'

class CreatePost(models.Model):
    picture = models.ImageField(upload_to='users/images', default='default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Author:{author}, title:{title}, picture:{picture}, date posted:{date_posted}"
