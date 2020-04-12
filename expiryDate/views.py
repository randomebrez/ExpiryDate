from django.shortcuts import render, redirect
from datetime import datetime
from .models import Produit
from .forms import RefForm, AjoutForm

def home(request):
    return render(request, 'base.html')

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'expiryDate/liste_produits.html', {'produits':produits})

def rechercheForm(request):
    form = RefForm(request.POST or None)
    if form.is_valid():
        reference = form.cleaned_data['reference']
    return render(request, 'expiryDate/rechercheForm.html', locals())

def rechercheProduit(request):
    form = RefForm(request.POST)
    if form.is_valid():
        reference = form.cleaned_data['reference']
    produit = Produit.objects.filter(reference=reference)
    if len(produit) == 0:
        template = "expiryDate/recherche_non_valide.html"
    else:
        template = "expiryDate/affiche_produit.html"
        produit = produit[0]
    return render(request, template, {'produit':produit}) 

def ajout(request):
    form = AjoutForm(request.POST or None)
    if form.is_valid():
        reference = form.cleaned_data['reference']
        date = form.cleaned_data['date']
    return render(request, 'expiryDate/ajoutForm.html', locals())

def checkProduit(request):
    form = AjoutForm(request.POST)
    if form.is_valid():
        reference = form.cleaned_data['reference']
        date = form.cleaned_data['date']
    produit = Produit.objects.filter(reference=reference)
    if len(produit) == 1:
        produit[0].expiryDate = date
        produit[0].save()
        template = "expiryDate/majProduit.html"
    else:
        produit = Produit.objects.create(reference=reference, expiryDate=date)
        produit.save()
        template = "expiryDate/produit_ajoute.html"
    return render (request, template)

