from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .forms import AutorForm
from .models import Autor
# Create your views here.




class Inicio(TemplateView):
    template_name="index.html"


class ListadoAutores(ListView):
   
    template_name= 'libro/listar_autor.html'
    queryset = Autor.objects.filter(estado = True)
    context_object_name='autores'


class ActualizarAutor(UpdateView):
    template_name="libro/crear_autor.html"
    model=Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")


class CrearAutor(CreateView):
    template_name='libro/crear_autor.html'
    model=Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")



class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy("libro:listar_autor")

    def post(self, request,pk,*args,**kwargs):
        object=Autor.objects.get(id = pk)
        object.estado=False
        object.save()

        return redirect('libro:listar_autor')



