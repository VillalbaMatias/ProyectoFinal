from django.shortcuts import render


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy #redireccion

from django.contrib.auth.views import LoginView, LogoutView

from .forms import  SingUpForm, UserEditForm
from .models import Post, Categoria, Autor

def mostrar_herencia(request):
    return render(request,'herencia.html')


#Registro de usuario 
class SingUpView(CreateView):

    form_class = SingUpForm
    success_url = reverse_lazy('Login')
    template_name = 'Login_Logout_Register/register.html'

#Inicio de sesion en el blog

class AdminLoginView(LoginView):

    template_name = 'Login_Logout_Register/login.html'

#Deslogueo de sesion en el blog
class AdmingLogoutView(LogoutView):

    template_name = 'Login_Logout_Register/logout.html'

#Creacion de post
class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('Home')
    fields = ['titulo','titulo_tag','autor','cuerpo','imagen','post_date','categoria']

#Visualizacion de Posts creados
class PostList(ListView):
    model = Post
    template_name = 'Blog/post_list.html'

#Detalle de cada Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    success_url = 'Blog/post_detail.html'
    fields = ['titulo','titulo_tag','autor','cuerpo','imagen','post_date','categoria']

class PostDeleteView(DeleteView):
    model = Post
    success_url = 'Blog/post_list.html'


#Vista basada en funcion, vista se encarga de poder editar el usuario logueado
def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            

            usuario.save()

            return render(request, 'herencia.html')

    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name':usuario.last_name
        })

    return render(request, 'Blog/profile_update.html', {
        'form': usuario_form,
        'username': usuario
    })


