from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('crear_autor/',login_required(CrearAutor.as_view()), name = 'crear_autor'),
    path('listar_autor/',login_required(ListadoAutores.as_view()), name = 'listar_autor'),
    path('editar_autor/<int:pk>/',login_required(ActualizarAutor.as_view()), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>/',login_required(EliminarAutor.as_view()), name = 'eliminar_autor'),


    path('listar_libro/',login_required(ListarLibros.as_view()),name="listar_libro"),
    path('crear_libro/',login_required(CrearLibro.as_view()), name = 'crear_libro'),
    path('editar_libro/<int:pk>',login_required(ActualizarLibro.as_view()), name = 'editar_libro'),
    path('eliminar_libro/<int:pk>',login_required(EliminarLibro.as_view()), name = 'eliminar_libro'),

    
]