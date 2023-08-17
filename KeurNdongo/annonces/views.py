from django.shortcuts import render

# annonces/views.py
from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceForm


from .models import Annonce

def accueil(request):
    annonces = Annonce.objects.order_by('-date_creation')
    # Code pour gérer les filtres (ville, quartier, prix, standing)
    context = {'annonces': annonces}
    return render(request, 'annonces/accueil.html', context)


def ajouter_annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.proprietaire = request.user
            annonce.save()
            return redirect('annonces:list')
    else:
        form = AnnonceForm()
    return render(request, 'annonces/ajouter_annonce.html', {'form': form})

