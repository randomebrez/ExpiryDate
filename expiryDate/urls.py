from django.urls import path
from . import views

urlpatterns = [
        path('', views.home),
        path('liste_produits/', views.liste_produits),
        path('recherche/', views.rechercheForm, name='recherche'),
        path('rechercheProduit/', views.rechercheProduit, name='rechercheProduit'),
        path('ajout/', views.ajout, name='ajout'),
        path('checkProduit/', views.checkProduit, name='checkProduit'),
        ]
