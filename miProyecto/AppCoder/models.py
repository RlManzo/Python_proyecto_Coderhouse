from django.db import models

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
