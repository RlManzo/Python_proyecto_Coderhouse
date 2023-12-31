from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario_datos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()    
    profesion = models.CharField(max_length=30)

class Juego(models.Model):
    nombre = models.CharField(max_length=30)  #tipo caracter
    año = models.IntegerField()  #tipo numeros enteros    

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

class Usuario_nuevo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
       

#clase para vincular el usuario con un avatar
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = "avatares", null=True, blank=True)
    