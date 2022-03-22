from django.db import models

# Create your models here.
class register(models.Model):
    UserName = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)
    Email =models.CharField(max_length=30)
    Password = models.CharField(max_length=20)

