from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    tel = models.CharField(max_length=15)
    is_student = models.BooleanField(default=True)

class Favoris(models.Model):
    annonce = models.ForeignKey('annonces.Annonce', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
