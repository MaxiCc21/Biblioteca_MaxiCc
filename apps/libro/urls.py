from django.urls import path
from .views import crearAutor,editarAutor,eliminarAutor,ListadoAutores,ActualizarAutor

urlpatterns = [
    path('crear_autor/',crearAutor, name = 'crear_autor'),
    path('listar_autor/',ListadoAutores.as_view(), name = 'listar_autor'),
    path('editar_autor/<int:pk>',ActualizarAutor.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor, name = 'eliminar_autor')
]