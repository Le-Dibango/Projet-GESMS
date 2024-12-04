from django.contrib import admin
from .models import (User)
from. models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["nom", "prenom", "etablissement__nom" ]
    list_display = ("nom", "prenom","etablissement","email", "is_student", "is_teacher", "is_educator",
                    "is_staff", "is_active")
    
@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    search_fields = ["nom", "prenom", "date_de_naissance","lieu_de_naissance"]
    list_display = ("nom", "prenom","genre","date_de_naissance","lieu_de_naissance","nationalite","matricule", "niveau","classe","mail_parent","is_student", "is_staff", "is_active")
    
@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    search_fields = ["nom", "prenom", "specialite"]
    list_display = ("nom", "prenom","genre","date_de_naissance","lieu_de_residence","nationalite" ,"specialite","contact","matricule","is_teacher","is_staff", "is_active")
  
    
@admin.register(Educateur)
class EducateurAdmin(admin.ModelAdmin):
    search_fields = ["nom", "prenom", "niveau"]
    list_display = ("nom", "prenom","niveau","etablissement","contact","email","is_educator","is_staff", "is_active")
    
    