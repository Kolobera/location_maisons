# user/urls.py
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('favoris/ajouter/<int:annonce_id>/', views.ajouter_favoris, name='ajouter_favoris'),
    path('favoris/', views.liste_favoris, name='favoris'),
    path('favoris/supprimer/<int:favori_id>/', views.supprimer_favori, name='supprimer_favori'),
    path('locations/resilier/<int:annonce_id>/', views.resilier_location, name='resilier_location'),
    path('tableau-de-bord/', views.tableau_de_bord, name='tableau_de_bord'),
]
