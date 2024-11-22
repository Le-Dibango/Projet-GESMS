from django import forms
from authentication.models import *

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = [
            'nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'nationalite',
            'genre', 'matricule', 'niveau', 'classe', 'contact',
            'nom_parent', 'profession_parent', 'lien_parente', 'contact_parent', 'photo'
        ]



class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = [
            'nom', 'prenom', 'date_de_naissance', 'lieu_de_residence', 'nationalite',
            'genre','specialite', 'matricule','contact','etablissement','photo'
        ]

