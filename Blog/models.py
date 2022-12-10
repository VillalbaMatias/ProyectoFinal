from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
        
    def get_absolute_url(self):
        return reverse('Home')
    

class Post(models.Model):
    titulo = models.CharField('Titulo',max_length=255)
    titulo_tag = models.CharField('Tag',max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField('Cuerpo',blank=True, null=True)
    post_date = models.DateField('Fecha de Creacion',default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField('Imagen', null= True, blank=True, upload_to='images/')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)



class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre de Autor',max_length=255, null= False, blank=False)
    apellido = models.CharField('Apellido de Autor',max_length=255, null= False, blank=False)
    correo = models.EmailField('Email',null=False, blank=False)

    def __str__(self):
        return f'Perfil de: {self.usuario}'
