# user/urls.py
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('favoris/ajouter/<int:annonce_id>/', views.ajouter_favoris, name='ajouter_favoris'),
    path('favoris/', views.liste_favoris, name='favoris'),
    # Autres URLs pour l'utilisateur
]
