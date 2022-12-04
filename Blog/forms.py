from django import forms
from .models import Post, Autor, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



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
        
class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        

class UserEditForm(UserCreationForm):

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

