from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Autor
from django.contrib.auth import get_user_model
from django.dispatch import receiver

usuario = get_user_model()

@receiver(post_save, sender=usuario)
def crear_autor(sender, instance, created, **kwargs):
    print("Sender -> ", sender)
    print("Instance -> ", instance)
    print("Created  -> ", created)


    if created:
        Autor.objects.create(
            usuario=instance,
            nombre=instance.first_name,
            apellido=instance.last_name,
            correo=instance.email
        ),print('Autor creado ')

