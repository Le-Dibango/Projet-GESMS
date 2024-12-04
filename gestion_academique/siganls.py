# gestion_academique/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Note
from authentication.models import *
from inscription.models import *


@receiver(post_save, sender=Note)
def envoyer_notification_parent(sender, instance, created, **kwargs):
    if created:  # Si une nouvelle note a été ajoutée
        eleve = instance.eleve  # Récupère l'élève concerné
        mail_parent = eleve.mail_parent  # Récupère l'email du parent
        if mail_parent:
            subject = f"Note de {eleve.prenom} {eleve.nom} - Devoir {instance.devoir.titre}"
            message = f"Bonjour {eleve.nom_parent},\n\nVotre enfant {eleve.prenom} {eleve.nom} a reçu une note de {instance.note} pour le devoir '{instance.devoir.titre}'."
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # L'email de l'expéditeur (configuré dans settings.py)
                [mail_parent],  # Destinataire : l'email du parent
                fail_silently=False,  # Si erreur, l'email échouera
            )
