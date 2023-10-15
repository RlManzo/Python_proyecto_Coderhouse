from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from AppCoder.models import *


#Clase para formulario de USER
class UsuarioRegistro(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email','first_name', 'last_name']    


class FormularioEditar(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['password1', 'password2','email','first_name', 'last_name']


#clase formulario avatar
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']
