from django.db import models
from django.utils import timezone
from datetime import datetime

class Produit(models.Model):
    reference = models.IntegerField(verbose_name = "Référence produit")
    expiryDate = models.DateTimeField(verbose_name = "Date d'expiration")

    class Meta :
        verbose_name = 'reference'
        ordering = ['expiryDate']

    def __int__(self):
        return self.reference

