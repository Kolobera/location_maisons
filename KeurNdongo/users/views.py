from django.http import HttpResponse
from django.shortcuts import render
# user/views.py
from django.shortcuts import render,redirect
from annonces.models import Annonce
from .models import Favoris




# user/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        
        #user = User.objects.get(username=username, password=password)
        if user is not None:
            context = {
            "user" : user,
        }
            # Connexion de l'utilisateur
            login(request, user)
            return render(request,'user/mon_compte.html',context)  # Remplacez par le nom de la vue souhaitée après la connexion
        else:
            # Authentification échouée
            return HttpResponse("Nom d'utilisateur ou mot de passe incorrect.")
      # Rediriger vers la page d'accueil ou une autre page
    else:
        
        return render(request, 'user/connexion.html')


# user/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from users.models import User

def inscription(request):
    if request.method == 'POST':
        user = User.objects.create(
            username = request.POST['username'],
            last_name = request.POST['nom'],
            first_name = request.POST['prenom'],
            tel = request.POST['tel'],
            email = request.POST['email'],
            password = request.POST['password'],
            is_student = True, #request.POST['est_etudiant'],
         
        )
        user.set_password(request.POST['password'])
        
        user.save()
            # Connexion automatique après l'inscription
        login(request, user)
        # return redirect('home')  # Rediriger vers la page d'accueil ou une autre page
    else:
        
        return render(request, 'user/inscription.html')


def ajouter_favoris(request, annonce_id):
    annonce = Annonce.objects.get(id=annonce_id)
    Favoris.objects.create(annonce=annonce, user=request.user)
    return redirect('user:favoris')

def liste_favoris(request):
    favoris = Favoris.objects.filter(user=request.user)
    return render(request, 'user/favoris_liste.html')

from django.contrib.auth.decorators import login_required
from annonces.models import Annonce

@login_required
def tableau_de_bord(request):
    proprietaire = request.user
    maisons = Annonce.objects.filter(proprietaire=proprietaire)
    nombre_maisons = maisons.count()
    nombre_maisons_louees = maisons.filter(louer=True).count()
    
    context = {
        'maisons': maisons,
        'nombre_maisons': nombre_maisons,
        'nombre_maisons_louees': nombre_maisons_louees,
        'nombre_maisons_non_louees': nombre_maisons - nombre_maisons_louees,
    }
    return render(request, 'user/tableau_de_bord.html', context)


@login_required
def mon_compte(request):
    user = request.user
    # profile_form = UserProfileForm(instance=user)
    
    annonces_locataire = Annonce.objects.filter(locataire=user)
    favoris = Favoris.objects.filter(user=user)
    
    # if request.method == 'POST':
    #     profile_form = UserProfileForm(request.POST, instance=user)
    #     if profile_form.is_valid():
    #         profile_form.save()
    #         return redirect('user:mon_compte')
    
    context = {
        'user': user,
        # 'profile_form': profile_form,
        'annonces_locataire': annonces_locataire,
        'favoris': favoris
    }
    return render(request, 'user/mon_compte.html', context)

@login_required
def supprimer_favori(request, favori_id):
    favori = Favoris.objects.get(id=favori_id)
    favori.delete()
    return redirect('user:mon_compte')

# user/views.py
@login_required
def resilier_location(request, annonce_id):
    annonce = Annonce.objects.get(id=annonce_id)
    annonce.locataire = None  # Supprimer le locataire de l'annonce
    annonce.save()
    return redirect('user:mon_compte')
