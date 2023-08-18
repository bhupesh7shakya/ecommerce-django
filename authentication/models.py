from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number=models.CharField(null=True,blank=True,max_length=10)
    
    def __str__(self) -> str:
        return f"{self.first_name}({self.username})"
    