
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from inscription.forms import EleveForm, EnseignantForm
from authentication.models import Eleve  # Assurez-vous que vous avez un modèle Eleve ou autre modèle où vous souhaitez enregistrer les données
from django.shortcuts import render, get_object_or_404
from authentication.models import *
from gestion_academique.models import *


def accueil(request):
    return render(request, 'accueil.html')

def reinit(request) :
    return render (request, 'reinit.html')

def accueil (request) :
    return render (request, 'accueil.html')

def Apropos (request) :
    return render (request, 'Apropos.html')

# vues spécifiques du templates 

def index(request):
    nombre_eleves = Eleve.objects.count()
    nombre_profs = Professeur.objects.count()
    # Combinez les deux variables dans un seul dictionnaire
    context = {
        'nombre_eleves': nombre_eleves,
        'nombre_profs': nombre_profs
    }
    return render(request, 'sites/index.html', context) # vues pour les membres de l'administration

def eleve(request) :
    return render (request, 'sites/index3.html') # vues pour les eleve

def prof(request) :
    eleves = Eleve.objects.all()  # Récupère tous les élèves
    return render(request, 'sites/index5.html', {'eleves': eleves})# vues pour les profs

def Liste_eleves(request) :
    eleve = Eleve.objects.all()
    print(eleve)
    return render (request, 'mes_eleves.html', context={'eleves':eleve}) # vues pour tous les étudiants


def toute_classe (request) :
    classe = Classe.objects.all()
    print(classe)
    return render (request, 'sites/all-class.html', context={'classes':classe}) # Toutes les classes 

def toutes_classes (request) :
    classe = Classe.objects.all()
    print(classe)
    return render (request, 'mes_classes.html', context={'classes':classe}) # Toutes les classes des rofs

def Liste_prof (request) :
    professeur = Professeur.objects.all()
    print(professeur)
    return render(request, 'sites/all-teacher.html', context = {'professeurs': professeur})

def Liste_parent (request) :
    parent = Eleve.objects.all()
    print(parent)
    return render(request, 'sites/all-parents.html', context={'eleves':parent})

# liste des élèves par classes ! 
def liste_classe_eleves(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    eleves = Eleve.objects.filter(classe=classe)
    return render(request, 'Liste_classe_eleve.html', {'classe': classe, 'eleves': eleves})







def prof_add (request) : 
    return render (request, 'sites/add-teacher.html') # ajout de prof

def eleve_add (request) :
    return render (request, 'sites/admit-form.html')

def reçu (request) :
    return render (request, 'sites/student-details.html') # reçu d'inscription

def detail_prof (request) :
    return render (request,'sites/teacher-details.html')




def eleve_add(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            # Récupérer les données validées
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            date_de_naissance = form.cleaned_data['date_de_naissance']
            lieu_de_naissance = form.cleaned_data['lieu_de_naissance']
            nationalite = form.cleaned_data['nationalite']
            genre = form.cleaned_data['genre']
            matricule = form.cleaned_data['matricule']
            niveau = form.cleaned_data['niveau']
            classe = form.cleaned_data['classe']
            contact = form.cleaned_data['contact']
            nom_parent = form.cleaned_data['nom_parent']
            profession_parent = form.cleaned_data['profession_parent']
            lien_parente = form.cleaned_data['lien_parente']
            contact_parent = form.cleaned_data['contact_parent']
            photo = form.cleaned_data['photo']
            # Vous pouvez également sauvegarder l'image et d'autres informations si nécessaire
            
            # Créer un nouvel objet Eleve ou un autre modèle
            eleve = Eleve(nom=nom, prenom=prenom,date_de_naissance=date_de_naissance,lieu_de_naissance=lieu_de_naissance,nationalite=nationalite,
                         genre=genre,matricule=matricule,niveau=niveau,classe=classe,contact=contact,nom_parent=nom_parent,
                         profession_parent=profession_parent,lien_parente=lien_parente,contact_parent=contact_parent,photo=photo)  # Ajoutez les autres champs ici
            eleve.save()  # Sauvegarder dans la base de données
            

            messages.success(request, 'Élève ajouté avec succès.')
            
            # Après l'enregistrement, rediriger vers une autre page (par exemple une page de succès)
            return redirect('sites/student-details.html')  # Remplacez 'page_succes' par l'URL de la page de succès
    else:
        form = EleveForm()

    return render(request, 'sites/admit-form.html', {'form': form})


def prof_add(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST, request.FILES)  # Inclure request.FILES pour gérer les fichiers comme la photo
        if form.is_valid():
            # Récupérer les données validées
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            date_de_naissance = form.cleaned_data['date_de_naissance']
            lieu_de_residence = form.cleaned_data['lieu_de_residence']
            nationalite = form.cleaned_data['nationalite']
            genre = form.cleaned_data['genre']
            specialite = form.cleaned_data['specialite']
            matricule = form.cleaned_data['matricule']
            contact = form.cleaned_data['contact']
            photo = form.cleaned_data['photo']

            # Créer un nouvel objet Professeur
            enseignant = Professeur(nom=nom,prenom=prenom,date_de_naissance=date_de_naissance, lieu_de_residence=lieu_de_residence,
                                    nationalite=nationalite,genre=genre, specialite=specialite,matricule=matricule,contact=contact,photo=photo
            )
            enseignant.save()  # Sauvegarder dans la base de données

            # Message de succès
            messages.success(request, 'Enseignant ajouté avec succès.')

            # Après l'enregistrement, rediriger vers une autre page (par exemple une page de détails des enseignants)
            return redirect('sites/teacher-details.html')  # Remplacez par le nom de votre URL de redirection
    else:
        form = EnseignantForm()

    return render(request, 'sites/add-teacher.html', {'form': form})


def eleve_detail(request, pk):
    eleve = get_object_or_404(Eleve, pk=pk)  
    return render(request, 'student-details.html', {'eleves': eleve})



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

def Specialité(request):
    context = {
        'Matière': MATIERE_CHOICES,
    }
    return render(request, 'add-teacher.html', context)



def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirection vers l'espace dédié
                if user.role == 'etudiant':
                    return redirect('etudiant_dashboard')
                elif user.role == 'enseignant':
                    return redirect('enseignant_dashboard')
                elif user.role == 'educateur':
                    return redirect('educateur_dashboard')
                elif user.role == 'parent':
                    return redirect('parent_dashboard')
    else:
        form = AuthenticationForm()
    messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, 'connexion.html', {'form': form})




def deconnexion (request):
    logout(request)
    return redirect('connexion')
