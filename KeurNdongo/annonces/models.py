from django.db import models

from django.db import models
from users.models import User

class Annonce(models.Model):
    TANDING_CHOICES = [
        ('standard', 'Standard'),
        ('moyen', 'Moyen'),
        ('haut', 'Haut'),
    ]

    titre = models.CharField(max_length=200)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annonces_proprietaire')
    locataire = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name='annonces_locataire')
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    standing = models.CharField(max_length=10, choices=TANDING_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    louer=models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')

