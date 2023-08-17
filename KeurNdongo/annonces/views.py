from django.utils import timezone
from django.shortcuts import render

# annonces/views.py
from django.shortcuts import render, redirect
from .models import Annonce
from django.contrib.auth.decorators import login_required


from .models import Annonce

def accueil(request):
    annonces = Annonce.objects.filter(louer=False).order_by('-date_creation')
    
    # Code pour gérer les filtres (ville, quartier, prix, standing)
    context = {'annonces': annonces}
    return render(request, 'annonces/accueil.html', context)

@login_required
def ajouter_annonce(request):
    if request.method == 'POST':
        
        annonce = Annonce.objects.create(
            titre = request.POST['titre'],
            proprietaire = request.user,
            ville = request.POST['ville'],
            quartier = request.POST['quartier'],
            prix = request.POST['prix'],
            description = request.POST['description'],
            standing = request.POST['standing'],
            date_creation =  timezone.now(),
            image = request.FILES['image'] 
        )
        annonce.save()
        return redirect('user:tableau_de_bord')
    else:
        
        return render(request, 'annonces/ajouter_annonce.html')

