from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('listar_usuario/',login_required(ListarUsuario_ListView.as_view()), name = 'listar_usuario'),
    path('crear_usuario/',login_required(CrearUsuario_CreateView.as_view()), name = 'crear_usuario'),
    path('editar_usuario/<int:pk>/',login_required(ActualizarUsuario_UpdateView.as_view()),name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/',login_required(EliminarUsuario_DeleteView.as_view()),name='eliminar_usuario')
]