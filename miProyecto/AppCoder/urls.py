from django.urls import path
from AppCoder.views import * 

urlpatterns = [
    path('inicio', inicio, name="Inicio"),
    path('profe', usuario_datos, name="UsuarioDatos"),
    path('crear_usuario', crear_usuario, name="Usuario"),
    path('busqueda_form', busqueda, name="BusquedaForm"),
    path('resultado', resultado_busqueda),
    path('favorito', agregar_favoritos, name="Favorito"),

    #borrar usuario
    path("borrar_usuario/<borrarUsuario>", borrar_usuario, name="borrarUser"),

    #formulario basado en clases/crear usuario
    path("crear_nuevo_usuario/", CrearUsuarioNuevo.as_view(), name="usuarioNuevo"),

    #actualizae
    path("actualizar_nuevo_usuario/<int:pk>", ActualizarUsuarioNuevo.as_view(), name="actualizarUsuarioNuevo"),

    #ver usuario nuevo
    path("ver_usuario_nuevo/", VerUsuarioNuevo.as_view(), name="verUsuarioNuevo"),

    #login
    path("login/",login , name="login"),
]