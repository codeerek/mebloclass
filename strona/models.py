from django.db import models
from django.utils import timezone

class Klienci(models.Model):
    imieNazwisko = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    opis = models.TextField()

    def __str__(self):
        return self.imieNazwisko


# Create your models here.
