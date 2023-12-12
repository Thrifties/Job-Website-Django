from django.db import models

# Create your models here.


class Admin_Account(models.Model):
    email = models.EmailField(
        max_length=255, unique=True, default='email@email.com')
    password = models.CharField(max_length=255, default='password')

    def __str__(self):
        return self.email
