from django import forms
from .models import Post, Autor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

#Formulario de registro de usuario
class SingUpForm(UserCreationForm):

    class Meta: 
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'username':'Nombre de Usuario',
            'email':'Mail',
            'password1':'Contraseña',
            'password2':'Confirmacion de la Contraseña'
        }

#Formulario para crear post
class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','autor','cuerpo','imagen','post_date','categoria']
        widgets = {
            'autor': forms.TextInput(attrs={'value':'', 'id':'autor', 'type':'hidden'}),
            
        }
#Formulario para actualizar el perfil del usuario
class UpdateUserForm(UserChangeForm):

    email = forms.EmailField(
        widget=forms.EmailInput
        (attrs={
            'class': 'form-control', 
            'placeholder': "Enter uour username"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': "Enter your first name"}))

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': "Enter your last name"}))

    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': "Enter your last name"}))
    
    class Meta:
        model = Autor
        fields = ['username', 'first_name', "last_name", 'email']

#Formulario de cambio de contraseña
class CambioPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Vieja contraseña'}))

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nueva contraseña'}))

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirme la nueva contraseña'}))
            
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']




