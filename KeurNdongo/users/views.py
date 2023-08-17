from django.shortcuts import render
# user/views.py
from django.shortcuts import render,redirect
from annonces.models import Annonce
from .models import Favoris




# user/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil ou une autre page
    else:
        form = AuthenticationForm()
    return render(request, 'user/connexion.html', {'form': form})


# user/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connexion automatique après l'inscription
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil ou une autre page
    else:
        form = UserCreationForm()
    return render(request, 'user/inscription.html', {'form': form})


def ajouter_favoris(request, annonce_id):
    annonce = Annonce.objects.get(id=annonce_id)
    Favoris.objects.create(annonce=annonce, user=request.user)
    return redirect('user:favoris')

def liste_favoris(request):
    favoris = Favoris.objects.filter(user=request.user)
    return render(request, 'user/favoris_liste.html', {'favoris': favoris})

from django.contrib.auth.decorators import login_required
from annonces.models import Annonce

@login_required
def tableau_de_bord(request):
    user = request.user
    annonces_locataire = Annonce.objects.filter(locataire=user)
    nombre_annonces_locataire = annonces_locataire.count()
    # Calculez d'autres statistiques nécessaires
    
    context = {
        'nombre_annonces_locataire': nombre_annonces_locataire,
        # Ajoutez d'autres statistiques au contexte
    }
    return render(request, 'user/tableau_de_bord.html', context)


@login_required
def mon_compte(request):
    user = request.user
    profile_form = UserProfileForm(instance=user)
    
    annonces_locataire = Annonce.objects.filter(locataire=user)
    favoris = Favoris.objects.filter(user=user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('user:mon_compte')
    
    context = {
        'user': user,
        'profile_form': profile_form,
        'annonces_locataire': annonces_locataire,
        'favoris': favoris
    }
    return render(request, 'user/mon_compte.html', context)