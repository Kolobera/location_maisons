# annonces/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('annonces/ajouter/', views.ajouter_annonce, name='ajouter'),
    path('', views.home, name="home"),
    # Autres URLs pour les annonces
]
