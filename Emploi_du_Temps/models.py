from django.db import models
from django.contrib import messages
from django.urls import reverse
import secrets
import sys
import string
from gestion_academique.models import *
from authentication.models import *

SALLES = (
        ('Salle 1', 'Salle 1',),
        ('Salle 2', 'Salle 2',),
        ('Salle 3', 'Salle 3',),
        ('Salle 4', 'Salle 4',),
        ('Salle 5', 'Salle 5',),
        ('Salle 6', 'Salle 6',),
        ('Salle 7', 'Salle 7',),
)

JOURS = (
        ('Lundi', 'Lundi',),
        ('Mardi', 'Mardi',),
        ('Mercredi', 'Mercredi',),
        ('Jeudi', 'Jeudi',),
        ('Vendredi', 'Vendredi',),
        ('Samedi', 'Samedi',),
        ('Dimanche', 'Dimanche',),
)


class EmploiDuTemps(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='emplois_du_temps')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.classe} - {self.date_update}'



class Programme(models.Model):
    date = models.DateField(null=True, blank=True) 
    classe = models.ForeignKey("gestion_academique.Classe", on_delete=models.CASCADE, related_name='Programme',blank=True, null=True)
    matiere = models.CharField(max_length=25, choices=MATIERE_CHOICES, blank=True, null=True)
    salle = models.CharField(max_length=25, choices=SALLES, blank=True, null=True)
    jour = models.CharField(max_length=25, choices=JOURS, blank=True, null=True)
    debut = models.CharField(max_length=5)
    fin = models.CharField(max_length=5)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='programmes')
    emploi_du_temps = models.ForeignKey(EmploiDuTemps, on_delete=models.CASCADE, related_name='programmes', null=True, blank=True)  # Ajout de la ForeignKey
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.matiere} ({self.jour}, {self.debut} - {self.fin})'
