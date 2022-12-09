from django.shortcuts import render
from django.http import HttpRequest


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy #redireccion

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView

from .forms import  SingUpForm, UpdateUserForm,CambioPasswordForm
from .models import Post, Categoria, Autor

from .forms import UpdateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class AutorCreateView(CreateView):
    model = Autor
    success_url = reverse_lazy('Home')
    fields = ['username','nombre','apellido','correo','fecha_creacion']


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

class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    form_class = UpdateUserForm
    login_url = 'login'
    template_name = "Autores/profile_update.html"
    success_url = reverse_lazy('Home')
    success_message = "User updated"

    def get_object(self):
        return self.request.user

    

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CambioPasswordForm
    login_url = 'login'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "Autores/password_change_success.html")



class Blog(HttpRequest):

    def about_us(request):
        return render(request,'Informacion/about.html')

    def mostrar_herencia(request):
        return render(request,'Informacion/herencia.html')

    def en_creacion(request):
            return render(request,'Informacion/en_creacion.html')
