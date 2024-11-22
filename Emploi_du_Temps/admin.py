from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('classe','matiere','salle','jour','debut', 'fin','professeur', 'active', 'created', 'date_update', )
    search_fields = ('matière','malle', 'professeur',)

class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 1  # Nombre de lignes supplémentaires affichées par défaut
    fields = ('date', 'matiere', 'salle', 'jour', 'debut', 'fin', 'professeur', 'active')
    readonly_fields = ('created', 'date_update')  # Optionnel pour afficher des champs en lecture seule
    show_change_link = True  # Permet de modifier directement un programme lié

# Admin d'EmploiDuTemps
@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('classe', 'active', 'created', 'date_update')
    inlines = [ProgrammeInline]
    search_fields = ('classe__nom',)  # Rechercher une classe par son nom
    list_filter = ('classe', 'active')  # Filtrer par classe ou statut actif
