from django.urls import path
from AppCoder.views import * 

urlpatterns = [
    path('inicio', inicio, name="Inicio"),
    path('profe', usuario_datos, name="UsuarioDatos"),
    path('crear_usuario', crear_usuario, name="Usuario"),
    path('busqueda_form', busqueda, name="BusquedaForm"),
    path('resultado', resultado_busqueda),
    path('favorito', agregar_favoritos, name="Favorito")
]