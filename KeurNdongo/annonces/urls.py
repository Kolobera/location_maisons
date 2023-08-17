# annonces/urls.py
from django.urls import path
from . import views

app_name = 'annonces'
urlpatterns = [
    path('ajouter/', views.ajouter_annonce, name='ajouter'),
    # Autres URLs pour les annonces
]
