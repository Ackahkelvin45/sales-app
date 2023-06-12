from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username=models.CharField(max_length=50,unique=True,null=True,blank=True)
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD='username'


    def __str__(self) :
        return self.username
    



