from django.core.mail import send_mail
from authentication.models import *  # Importez le modèle Parent

def envoyer_email(sujet, message, destinataire):
    emails = Eleve.objects.values_list('mail', flat=True)  
    send_mail(
        sujet,
        message,
        'gesms.edu01@gmail.com',  # Adresse expéditeur
        list(emails),  # Liste des emails des parents
        fail_silently=False,
    )
