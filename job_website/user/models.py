from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, default='email@email.com')
    password = models.CharField(max_length=255, default='password')
    
    def __str__(self):
        return self.username
    
class Employee(models.Model):
    email = models.EmailField(max_length=255, unique=True, default="email@email.com")
    password = models.CharField(max_length=255, default='password')
    def __str__(self):
        return self.first_name + ' ' + self.last_name