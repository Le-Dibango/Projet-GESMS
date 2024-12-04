from django.shortcuts import render, redirect
from django.core.mail import send_mail
from authentication.models import *
from gestion_academique.models import *
from .forms import EtatPresenceForm
from django.core.mail import BadHeaderError
from inscription.forms import *
from gestion_academique.tasks import envoyer_email_parent
from django.utils.timezone import now
from datetime import date

def liste_appel(request):
    eleves = Eleve.objects.all()
    # professeur = Professeur.objects.get()
    # cours = Cours.objects.get()
    if request.method == 'POST':
        for eleve in eleves:
            etat_presense = request.POST.get(f'etat_presense_{eleve.id}')
            if etat_presense:
                # Enregistrer la présence
                EtatPresence.objects.create(
                    eleve=eleve,
                    etat_presense=etat_presense,
                    date=date.today(),
                    heure_debut=now().time(),
                    heure_fin=now().time(),
                    professeur=Professeur.nom,  # Exemple : professeur connecté
                    cours =MATIERE_CHOICES
                )

                # Envoyer un e-mail si absent ou en retard
                if etat_presense in ['absent', 'en_retard']:
                    recipient_list = [eleve.mail_parent] if eleve.mail_parent else []
                    if recipient_list:
                        envoyer_email_parent.delay(
                                    eleve.mail_parent,
                                    eleve.nom,
                                    eleve.prenom,
                                    etat_presense,
                                    Cours,  # Assurez-vous que cette variable est définie
                                    Professeur # Assurez-vous que cette variable est définie
)
        return redirect('confirmation_appel')

    return render(request, 'liste_appel.html', {'eleves': eleves})

def confirmation_appel(request) :
    return render (request, 'confirmation_appel.html')





