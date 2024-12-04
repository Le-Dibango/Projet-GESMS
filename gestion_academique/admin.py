from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(AnneeScolaire)
class AnneeScolaireAdmin(admin.ModelAdmin):
    list_display = ('etablissement', 'debut', 'fin', 'active', 'created', 'date_update', )
    search_fields = ('etablissement__nom','debut', 'fin',)



@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    search_fields = ['nom']
    list_display = ('logo_image','nom','sigle','code','active', 'created', 'date_update')
    search_fields = ('nom',)

    def logo_image(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.logo.url)
        return "Pas de logo"
    logo_image.short_description = 'Logo'





@admin.register(Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    search_fields = ['nom_du_chapitre']
    list_display = ('matiere','niveau','classe','nom_du_chapitre','numéro_du_chapitre','description')
    search_fields = ('nom_du_chapitre','niveau')


@admin.register(LesNiveau)
class LesNiveauAdmin(admin.ModelAdmin):
    search_fields = ['Niveau']
    list_display = ('Niveau','description','Etablissement')
    search_fields = ('Niveau',)


@admin.register(LesMatiere)
class LesMatiereAdmin(admin.ModelAdmin):
    search_fields = ['Matiere']
    list_display = ('Matiere','abreviation','coefficient', 'niveau')
    search_fields = ('Matiere','abreviation')


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    search_fields = ['Titre_du_cours']
    list_display = ('Année_Scolaire','matiere','Titre_du_cours','date_publication', 'niveau','Resumé')
    search_fields = ('Titre_du_cours','date_publication')
 

@admin.register(Devoir)
class DevoirAdmin(admin.ModelAdmin):
    search_fields = ['type']
    list_display = ('niveau','classe','matiere','chapitre','type','trimestre','Coefficient','date')
    search_fields = ('type','date')
    


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    search_fields = ['Nom']
    list_display = ('Nom','niveau','Année_Scolaire','Etablissement','description')
    search_fields = ('Nom',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['eleve']
    list_display = ('niveau','classe','valeur','eleve','devoir','trimestre','type')
    search_fields = ('eleve',)

@admin.register(Resultat)
class ResultatAdmin(admin.ModelAdmin):
    search_fields = ['eleve']
    list_display = ('moyenne_generale','eleve','date','trimestre','niveau')
    search_fields = ('eleve',)


@admin.register(EtatPresence)
class EtatPresenceAdmin(admin.ModelAdmin):
    search_fields = ['cours','eleve']
    list_display = ('cours','date','eleve','heure_debut','heure_fin','Professeur','etat_presense',)
    search_fields = ('eleve',)