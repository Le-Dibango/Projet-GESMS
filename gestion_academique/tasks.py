from celery import shared_task
from django.core.mail import send_mail
from datetime import date
from authentication.models import *
from gestion_academique.models import *
import logging
logger = logging.getLogger(__name__)


@shared_task
def envoyer_email_parent(mail_parent, nom, prenom, etat_presence, matiere, professeur):
    try:

        sujet = f"État de présence de {nom} {prenom}"
        message = (
        f"Bonjour,\n\n"
        f"Nous tenons à vous informer que votre enfant {nom} {prenom} était : {etat_presence}.\n"
        f"Au cours de : {matiere} (Professeur : {professeur}).\n"
        f"Date : {date.today()}.\n\n"
        f"Cordialement."
    )
        from_email = 'gesms.edu01@gmail.com'
        
        # Envoi de l'email
        send_mail(sujet, message, from_email, [mail_parent])
        
        # Log de succès
        logger.info(f"Email envoyé avec succès à {mail_parent}.")
    
        # Code d'envoi
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'email : {e}")
