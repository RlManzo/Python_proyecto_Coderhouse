from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from AppCoder.models import *
from django import forms
from django.contrib.auth.models import User


def nuevo_profesor(request):
    profe = Usuario_datos(nombre="ricardo",apellido="manzo",email="rl_manzo@gmail.com",profesion="frontend")
    profe.save()

    return HttpResponse("hemos guardado al profesor")

def inicio(request):
     return render(request, "AppCoder/inicio.html")

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

def agregar_favoritos(request):
    if request.method == 'POST':
         favorito = Juego(nombre=request.POST['nombre'],año=request.POST['año'])
         favorito.save()
         return render(request, 'AppCoder/inicio.html')
    return render(request, 'AppCoder/favorito.html')

#Funciones tipo GET buscar en BD

def busqueda(request):
    return render(request, "AppCoder/busqueda_form.html")

def resultado_busqueda(request):
     if request.GET['nombre']:
         nombre = request.GET['nombre']
         resultado_usuario = Usuario.objects.filter(nombre__icontains=nombre)
         return render(request, "AppCoder/resultado.html", {"valor":nombre, "res": resultado_usuario})
     else:
         return HttpResponse("usuario incorrecto o no valido")
     
     return render(request, "AppCoder/resultado.html")

#borrar usuario boton
def borrar_usuario(request, borrarUsuario):
    usuario_elegido = Usuario.objects.get(nombre=borrarUsuario)
    usuario_elegido.delete()
    todos = Usuario.objects.all()

    return render(request, "AppCoder/inicio.html")


#crud con clases
#create
class CrearUsuarioNuevo(CreateView):   #usuario_nuevo_form.html
      model = Usuario_nuevo
      fields = ["nombre","apellido", "password","email"]
      success_url = "/AppCoder/inicio"

#update
class ActualizarUsuarioNuevo(UpdateView):   #usuario_nuevo_form.html
      model = Usuario_nuevo
      fields = ["nombre","apellido", "password","email"]
      success_url = "/AppCoder/inicio"      

#read
class VerUsuarioNuevo(ListView): #usuario_nuevo_list.html
     model= Usuario_nuevo



#inciar sesion con una funcion

def login(request):
    if request.method == "POST": 
      form_inicio = AuthenticationForm(request, data = request.POST)

      if form_inicio.is_valid():
          info = form_inicio.changed_data()
          usuario = info.get('username')
          contra = info.get('password')

          user = authenticate(username=usuario, password=contra)
          if user:
             login(request, user) 

             return render(request,"AppCoder/inicio.html",{"usuario": user})
          
          else:
             
             return render(request, "AppCoder/login.html", {"mensaje": "datos incorrectos"})  
    form_inicio = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form_inicio})      