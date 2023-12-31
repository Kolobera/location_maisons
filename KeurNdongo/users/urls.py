# user/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('mon-compte/', views.mon_compte, name='mon_compte'),
    path('favoris/ajouter/<int:annonce_id>/', views.ajouter_favoris, name='ajouter_favoris'),
    path('favoris/', views.liste_favoris, name='favoris'),
    path('favoris/supprimer/<int:favori_id>/', views.supprimer_favori, name='supprimer_favori'),
    path('locations/resilier/<int:annonce_id>/', views.resilier_location, name='resilier_location'),
    path('tableau-de-bord/', views.tableau_de_bord, name='tableau_de_bord'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('supprimer_annonce/<int:annonce_id>', views.supprimer_annonce, name='supprimer_annonce') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
