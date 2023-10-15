from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from AppCoder.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *

#vista inicio
def inicio(request):
     return render(request, "AppCoder/inicio.html")


##########CRUD por funciones###########
#######################################

#Crear en BD
def usuario_datos(request):
     if request.method == 'POST':
         profe = Usuario_datos(nombre=request.POST['nombre'],apellido=request.POST['apellido'], email=request.POST['email'],profesion=request.POST['profesion'])
         profe.save()
         return render(request, 'AppCoder/inicio.html')
     return render(request, 'AppCoder/profe.html')

def crear_usuario(request):
     if request.method == 'POST':
         profe = Usuario(nombre=request.POST['nombre'],password=request.POST['password'], email=request.POST['email'])
         profe.save()
         return render(request, 'AppCoder/inicio.html')
     return render(request, "AppCoder/crear_usuario.html")

@login_required
def agregar_favoritos(request):
    if request.method == 'POST':
         favorito = Juego(nombre=request.POST['nombre'],año=request.POST['año'])
         favorito.save()
         return render(request, 'AppCoder/inicio.html')
    return render(request, 'AppCoder/favorito.html')


#Funciones tipo GET buscar en BD

def busqueda(request):
    return render(request, "AppCoder/busqueda_form.html")

#Vista buscador
def resultado_busqueda(request):
     if request.GET['nombre']:
         nombre = request.GET['nombre']
         resultado_usuario = Usuario.objects.filter(nombre__icontains=nombre)
         return render(request, "AppCoder/resultado.html", {"valor":nombre, "res": resultado_usuario})
     else:
         return HttpResponse("usuario incorrecto o no valido")
     
     return render(request, "AppCoder/resultado.html")

#Borrar usuario boton
def borrar_usuario(request, borrarUsuario):
    usuario_elegido = Usuario.objects.get(nombre=borrarUsuario)
    usuario_elegido.delete()
    todos = Usuario.objects.all()

    return render(request, "AppCoder/inicio.html")


##############CRUD con clases#################
##############################################


#Create
class CrearUsuarioNuevo(LoginRequiredMixin, CreateView):   #usuario_nuevo_form.html
      model = Usuario_nuevo
      fields = ["nombre","apellido", "password","email"]
      success_url = "/AppCoder/inicio"

#Update
class ActualizarUsuarioNuevo(LoginRequiredMixin, UpdateView):   #usuario_nuevo_form.html
      model = Usuario_nuevo
      fields = ["nombre","apellido", "password","email"]
      success_url = "/AppCoder/inicio"      

#Read
class VerUsuarioNuevo(LoginRequiredMixin, ListView): #usuario_nuevo_list.html
     model= Usuario_nuevo

#Delete
class EliminarUsuarioNuevo(LoginRequiredMixin,DeleteView):
    model = Usuario_nuevo



#iniciar sesion con una funcion

def iniciar_sesion(request):
    if request.method == "POST": 
      form = AuthenticationForm(request, data = request.POST)

      if form.is_valid():
         # info = form_inicio.changed_data()
          usuario = form.cleaned_data.get('username')
          contra = form.cleaned_data.get('password')

          user = authenticate(username=usuario, password=contra)
          if user:
             login(request, user) 

             return render(request,"AppCoder/inicio.html",{"usuario": f"bienvenido {user}" })
          
      else:
         return render(request, "AppCoder/login.html", {"form": form,"mensaje": "datos incorrectos"})  
    else:      
        form_inicio = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form_inicio})      


#register

#vista registro

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UsuarioRegistro(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado"})

      else:
            #form = UserCreationForm()       
            form = UsuarioRegistro()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

#Editar datos usuario

@login_required
def editarUsuario(request):
     usuario = request.user

     if request.method == "POST":
          form = FormularioEditar(request.POST)
          if form.is_valid(): 
             info = form.cleaned_data()

             usuario.email = info["email"] 
             usuario.set_password(info["password"])
             usuario.first_name = info["first_name"]
             usuario.last_name = info["last_name"]

             usuario.save()

             return render(request, "AppCoder/inicio.html" , {"mensaje":"usuario eliminado"} )
     else: 
        form = FormularioEditar(initial = {
            "email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name
        })   
     return render(request, "AppCoder/editarPerfil.html", {"form": form, "usuario": usuario})


#editar img Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()

            return render(request, "AppCoder/inicio.html")
    else:

        form = AvatarFormulario()
    
    return render(request, "AppCoder/agregarAvatar.html",{"form": form})