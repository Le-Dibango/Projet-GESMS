from django.db import models
from gestion_academique.models import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from gestion_academique.models import MATIERE_CHOICES
from gestion_academique.models import Etablissement


class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField(unique=True, null=True)
    etablissement = models.ForeignKey('gestion_academique.Etablissement', related_name="user_etablissement", on_delete=models.CASCADE, null=True, blank=True)
    
    is_staff = models.BooleanField(
         _("AUTORISER AU SITE"),
        default=False,
        help_text=_('Indique si l"utilisateur peut se connecter à ce site.'),
    )
    is_super_admin = models.BooleanField(
        _("SUPER ADMINISTRATEUR"),
        default=False,
        help_text=_('Indique si l"utilisateur est super administrateur .'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']
   
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

    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Indique si cet utilisateur doit être traité comme actif. '
            "Désélectionner ceci au lieu de supprimer des comptes."
        ),
    )

    is_student = models.BooleanField(
        _('ÉTUDIANT'),
        default=False,
        help_text=_('Cocher si l"utilisateur est un étudiant.'),
    )

    is_teacher = models.BooleanField(
        _('ENSEIGNANT'),
        default=False,
        help_text=_('Cocher si l"utilisateur est un enseignant.'),
    )
    
    is_educator = models.BooleanField(
        _('EDUCATREUR'),
        default=False,
        help_text=_('Cocher si l"utilisateur est un éducateur.'),
    )


    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    
Sexe  = (
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    )
    
Pays_choices = (

        ('Afrique du Sud','Afrique du Sud'),
        ('Allemagne','Allemagne'),
        ('Algérie','Algérie'),
        ('Angola','Angola'),
        ('Autriche','Autriche'),
        ('Bénin','Bénin'),
        ('Belgique','Belgique'),
        ('Bulgarie','Bulgarie'),
        ('Burkina Faso','Burkina Faso'),
        ('Cameroun','Cameroun'),
        (" Côte d'Ivoire","Côte d'Ivoire"),
        ('Danemark', 'Danemark'),
        ('Espagne','Espagne'),
        ('France','France'),
        ('Ghana','Ghana'),
        ('Grèce','Grèce'),
        ('Hongrie', 'Hongrie'),
        ('Irlande','Irlande'),
        ('Italie','Italie'),
        ('Kenya','Kenya'),
        ('Maroc','Maroc'),
        ('Nigeria','Nigeria'),
        ('Pays-Bas','Pays-Bas'),
        ('Pologne','Pologne'),
        ('Portugal','Portugal'),
        ('Sénégal','Sénégal'),
        ('Suède','Suède'),
        ('Tunisie','Tunisie'),
        ('Zambie','Zambie'),

)

  # Modèle Elève  
class Eleve(User):
    date_de_naissance = models.DateField(null=True, blank=True)
    lieu_de_naissance = models.CharField(max_length=255, null=True, blank=True)
    nationalite = models.CharField(max_length=25, choices= Pays_choices, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')], null=True, blank=True)
    matricule = models.CharField(max_length=10, null=True, blank=True)
    niveau = models.ForeignKey("gestion_academique.LesNiveau", on_delete=models.CASCADE,related_name='Eleve',null=True, blank=True)
    classe = models.ForeignKey("gestion_academique.Classe", on_delete=models.CASCADE, related_name='Eleve',null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    nom_parent = models.CharField(max_length=255, null=True, blank=True)
    profession_parent = models.CharField(max_length=100, null=True, blank=True)
    lien_parente = models.CharField(max_length=50, choices=[('Père', 'Père'), ('Mère', 'Mère'), ('Tuteur', 'Tuteur')], null=True, blank=True)
    contact_parent = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='photos_eleves/', null=True, blank=True)
    photo_parent = models.ImageField(upload_to='photos_eleves/', null=True, blank=True)

    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"
    
    def save(self, *args, **kwargs):
        self.is_student = True  
        super().save(*args, **kwargs)


# Modèle Prof
class Professeur(User):
    specialite = models.CharField(max_length=25, choices= MATIERE_CHOICES, blank=True, null=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    lieu_de_residence = models.CharField(max_length=255, null=True, blank=True)
    nationalite = models.CharField(max_length=25, choices= Pays_choices, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')], null=True, blank=True)
    matricule = models.CharField(max_length=10, null=True, blank=True)
    photo = models.ImageField(upload_to='photos_prof/', null=True, blank=True)

    class Meta:
        verbose_name = "Professeur"
        verbose_name_plural = "Professeurs"
    
    def save(self, *args, **kwargs):
        self.is_teacher = True  # Marquer cet utilisateur comme un enseignant
        super().save(*args, **kwargs)


# Modèle Educateurs
class Educateur(User):
    contact = models.CharField(max_length=20, null=True, blank=True)
    niveau = models.ForeignKey('gestion_academique.LesNiveau',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = "Éducateur"
        verbose_name_plural = "Éducateurs"
    
    def save(self, *args, **kwargs):
        self.is_educator = True  # Marquer cet utilisateur comme un éducateur
        super().save(*args, **kwargs)
