from django.shortcuts import render

# annonces/views.py
from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceForm

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

