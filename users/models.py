from django.db import models

# Create your models here.

class UsersProfile(models.Model):

    gender = [ ('M' , 'Male'), ('F' , 'Female') ]

    name = models.CharField(max_length=50)
    sec_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=120, choices=gender)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f'users name:{self.name}, email:{self.email}, phone_number:{self.phone_number}'
