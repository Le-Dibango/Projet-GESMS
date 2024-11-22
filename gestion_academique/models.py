from django.db import models
from django.contrib import messages
from django.urls import reverse
import secrets
import sys
import string
from authentication.models import *

cycles = (

    ('CONTINU', 'CONTINU',),
    ('ONLINE', 'ONLINE',),
    ('PROFESSIONNEL', 'PROFESSIONNEL',),
    ('UNIVERSITAIRE', 'UNIVERSITAIRE',),

)

cycles_diplomes = (

    ('PROFESSIONNEL', 'PROFESSIONNEL',),
    ('UNIVERSITAIRE', 'UNIVERSITAIRE',),

)

niveau_diplomes = (

    ('LICENCE', 'LICENCE',),
    ('MASTER', 'MASTER',),

)

type_filieres = (

    ('UNIVERSITAIRE', 'UNIVERSITAIRE',),
    ('PROFESSIONNEL', 'PROFESSIONNEL',),
    

)

jours = (
        ('Lundi', 'Lundi',),
        ('Mardi', 'Mardi',),
        ('Mercredi', 'Mercredi',),
        ('Jeudi', 'Jeudi',),
        ('Vendredi', 'Vendredi',),
        ('Samedi', 'Samedi',),
        ('Dimanche', 'Dimanche',),
)

session = (
    ('SESSION 1', 'SESSION 1',),
    ('SESSION 2', 'SESSION 2',)

)

semestre = (
    ('SEMESTRE 1', 'SEMESTRE 1',),
    ('SEMESTRE 2', 'SEMESTRE 2',),
    ('SEMESTRE 3', 'SEMESTRE 3',)

)

categories_ue = (

    ('CONNAISSANCE FONDEMENTALE', 'CONNAISSANCE FONDEMENTALE',),
    ('METHODOLOGIE', 'METHODOLOGIE',),
    ('CULTURE GENERALE', 'CULTURE GENERALE',),

)

class Etablissement(models.Model):
    """Model definition for Etablissement."""
    nom = models.CharField(max_length=150)
    sigle = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    nom_complet = models.TextField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    cachet_scolarite = models.FileField(upload_to='etablissement/cachez_scolarite',null=True, blank=True)
    footer_bull = models.TextField()
    contact = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    # site = models.EmailField(max_length=254)
    active = models.BooleanField(default=True)
    is_college = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    wave_api_key = models.TextField(null=True, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Etablissement."""

        verbose_name = 'Etablissement'
        verbose_name_plural = 'Etablissements'

    def __str__(self):
        """Unicode representation of Etablissement."""
        return self.nom_complet 
    
    

class AnneeScolaire(models.Model):
    """Model definition for AnneeScolaire."""
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="AnneeScolaire")
    debut = models.IntegerField()
    fin = models.IntegerField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for AnneeScolaire."""

        verbose_name = 'Année Scolaire'
        verbose_name_plural = 'Années Academiques'

    def __str__(self):
        """Unicode representation of AnneeScolaire."""
        return f'{self.debut} - {self.fin}'


    @property
    def annees(self):
        """Unicode representation of AnneeScolaire."""
        return f'{self.debut}-{self.fin}'

   


# Modèle pour les Niveaux
class LesNiveau(models.Model):
    Niveau_CHOICES = [
        ('6ème', '6ème'),
        ('5ème', '5ème'),
        ('4ème', '4ème'),
        ('3ème', '3ème'),
        ('2nd', ('2nd')),
        ('1ère', ('1ère')),
        ('Tle', ('Tle')),  
    ]  
    Niveau = models.CharField(
        max_length=50,
        choices=Niveau_CHOICES,
        default='6ème',
        )
    description = models.TextField(blank=True, null=True)
    Etablissement =models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Niveau
    

    

  
# Modèle pour les Matières
class LesMatiere(models.Model):
    MATIERE_CHOICES = [
        ('Maths', 'Mathématiques'),
        ('SVT', 'Sciences de la Vie et de la Terre'),
        ('PC', 'Physique-Chimie'),
        ('HG', 'Histoire-Géographie'),
        ('Français', ('Français')),
        ('Anglais', ('Anglais')),
        ('Espagnol', ('Espagnol')),
        ('Allemand', ('Allemand')),
        ('Edhc', ('Edhc')),
        ('Eps', ('Eps')),
        ('Musique', ('Musique')),
        ('AP', ('Art-plastique')),
        ('Philo',('Philosophie')), 
        ('Ent', ('Entrepreuneuriat')),  
    ]  
    Matiere = models.CharField(
        max_length=50,
        choices=MATIERE_CHOICES,
        default='Mathématiques',
    )
    abreviation = models.CharField(max_length=10, unique=True)
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE, related_name='Matiere')
    coefficient = models.IntegerField()
    
    def __str__(self):
        return f"{self.Matiere} "

       

MATIERE_CHOICES = (
        ('Maths', 'Mathématiques'),
        ('SVT', 'Sciences de la Vie et de la Terre'),
        ('PC', 'Physique-Chimie'),
        ('HG', 'Histoire-Géographie'),
        ('Français', 'Français'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Allemand', 'Allemand'),
        ('Edhc', 'Edhc'),
        ('Eps', 'Eps'),
        ('Musique', 'Musique'),
        ('AP', 'Art-plastique'),
        ('Philo','Philosophie'), 
        ('Ent', 'Entrepreuneuriat'),
)  


   




# Modèle pour les Classes
class Classe(models.Model):
    Etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name='classes')
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE, related_name='classes')
    Nom = models.CharField(max_length=50)
    Professeur_principal = models.ForeignKey('authentication.Professeur', on_delete=models.CASCADE,null=True,blank=True)
    Spécialité_du_prof = models.CharField(max_length=20, choices=MATIERE_CHOICES, blank=True, null=True)
    Année_Scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,)
    description = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return f" {self.Nom}"

#Modèle pour les Chapitres 
class Chapitre (models.Model) :
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE, related_name='Chapitre')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='Chapitre')
    matiere = models.ForeignKey(LesMatiere, on_delete=models.CASCADE, related_name='Chapitre')
    nom_du_chapitre = models.CharField(max_length=100)
    numéro_du_chapitre = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.nom_du_chapitre} - {self.numéro_du_chapitre} {self.matiere}"

TYPE_CHOICES = (
    ('Interrogation', 'Interrogation',),
    ('Devoir de niveau', 'Devoir de niveau',),
    ('Devoir de classe ', 'Devoir de classe',)
) 

TRIMESTRE_CHOICES = (
    ('TRIMESTRE 1', 'TRIMESTRE 1',),
    ('TRIMESTRE 2', 'TRIMESTRE 2',),
    ('TRIMESTRE 3', 'TRIMESTRE 3',)
)

MATIERE_CHOICES = (
        ('Maths', 'Mathématiques'),
        ('SVT', 'Sciences de la Vie et de la Terre'),
        ('PC', 'Physique-Chimie'),
        ('HG', 'Histoire-Géographie'),
        ('Français', 'Français'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Allemand', 'Allemand'),
        ('Edhc', 'Edhc'),
        ('Eps', 'Eps'),
        ('Musique', 'Musique'),
        ('AP', 'Art-plastique'),
        ('Philo','Philosophie'), 
        ('Ent', 'Entrepreuneuriat'),
)  

# Modèle pour les Devoirs
class Devoir(models.Model):
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE, related_name='Devoir')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='Devoir')
    matiere = models.ForeignKey(LesMatiere, on_delete=models.CASCADE, related_name='Devoir')
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE,related_name='Devoir')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)
    trimestre = models.CharField(max_length=20,choices=TRIMESTRE_CHOICES, blank=True, null=True)
    Coefficient = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f" {self.matiere} {self.chapitre} - {self.type} {self.trimestre}"
    


    # Modèle pour les Notes
class Note(models.Model):
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE, related_name='note',default='default_value')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='note')
    devoir = models.ForeignKey(Devoir, on_delete=models.CASCADE, related_name='note')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)
    trimestre = models.CharField(max_length=20,choices=TRIMESTRE_CHOICES, blank=True, null=True)
    eleve = models.ForeignKey('authentication.Eleve', on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.eleve} - {self.valeur} {self.devoir}"


# Modèle pour les Cours
class Cours(models.Model):
    Année_Scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,)
    matiere = models.ForeignKey(LesMatiere, on_delete=models.CASCADE, related_name='cours')
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE,)
    Professeur = models.ForeignKey('authentication.Professeur',on_delete=models.CASCADE, related_name='Cours',null=True, blank=True)
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE,related_name='cours')
    Titre_du_cours = models.CharField(max_length=100)
    Resumé = models.TextField()
    date_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.matiere} {self.chapitre} - {self.Titre_du_cours}"


# Modèle pour les Résultats
class Resultat(models.Model):
    niveau = models.ForeignKey(LesNiveau, on_delete=models.CASCADE,)
    trimestre = models.CharField(max_length=20,choices=TRIMESTRE_CHOICES, blank=True, null=True)
    eleve = models.ForeignKey('authentication.Eleve', on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='resultat')
    moyenne_generale = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f" {self.niveau} {self.trimestre} - {self.classe} {self.moyenne_generale}"
    
