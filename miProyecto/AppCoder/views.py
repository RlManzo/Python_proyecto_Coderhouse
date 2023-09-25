from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

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
