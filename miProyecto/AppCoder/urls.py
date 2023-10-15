from django.urls import path
from AppCoder.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', inicio, name="Inicio"),
    
#CRUD funciones
    #create 
    path('profe', usuario_datos, name="UsuarioDatos"),
    path('crear_usuario', crear_usuario, name="Usuario"),
    path('favorito', agregar_favoritos, name="Favorito"),
    #read
    path('busqueda_form', busqueda, name="BusquedaForm"),
    path('resultado', resultado_busqueda),
    #borrar usuario
    path("borrar_usuario/<borrarUsuario>", borrar_usuario, name="borrarUser"),
#CRUD clases
    #formulario basado en clases/crear usuario
    path("crear_nuevo_usuario/", CrearUsuarioNuevo.as_view(), name="usuarioNuevo"),
    #actualizar
    path("actualizar_nuevo_usuario/<int:pk>", ActualizarUsuarioNuevo.as_view(), name="actualizarUsuarioNuevo"),
    #ver lista de usuarios nuevos
    path("ver_usuario_nuevo/", VerUsuarioNuevo.as_view(), name="verUsuarioNuevo"),

    #register
    path("register/", register, name="register"),
    #login
    path("login/",iniciar_sesion , name="login"),
    #logout
    path('logout', LogoutView.as_view(template_name = "AppCoder/logout.html"), name= "Logout"),
    #editar
    path('editar/', editarUsuario, name="EditarUsuario"),
    #agregar avatar
    path("agregarAvatar/", agregarAvatar, name="avatar")
]