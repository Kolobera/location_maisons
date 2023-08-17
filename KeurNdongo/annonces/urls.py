# annonces/urls.py
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('annonces/ajouter/', views.ajouter_annonce, name='ajouter'),
    path('', views.accueil, name="home"),
    # Autres URLs pour les annonces
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
