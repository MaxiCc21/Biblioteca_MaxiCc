from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('listar_usuario/',login_required(ListarUsuario_ListView.as_view()), name = 'listar_usuario'),
    path('crear_usuario/',login_required(CrearUsuario_CreateView.as_view()), name = 'crear_usuario'),
]