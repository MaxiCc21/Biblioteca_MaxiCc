from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .forms import AutorForm, LibroForm
from .models import Autor, Libro
# Create your views here.

class Inicio(TemplateView):
    template_name="index.html"


class ListadoAutores(ListView):
    template_name= 'autor/listar_autor.html'
    queryset = Autor.objects.filter(estado = True)
    context_object_name='autores'


class ActualizarAutor(UpdateView):
    template_name="autor/crear_autor.html"
    model=Autor
    form_class = AutorForm
    success_url = reverse_lazy("librolistar_autor")


class CrearAutor(CreateView):
    template_name='autor/crear_autor.html'
    model=Autor
    form_class = AutorForm
    success_url = reverse_lazy("librolistar_autor")

class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy("libro:listar_autor")

    def post(self, request,pk,*args,**kwargs):
        object=Autor.objects.get(id = pk)
        object.estado=False
        object.save()

        return redirect('libro:listar_autor')

######################################################################################################################

class ListarLibros(ListView):
    template_name='libro/listar_libro.html'
    queryset = Libro.objects.filter(estado = True)
    context_object_name = "libros"



class CrearLibro(CreateView):
    model=Libro
    template_name="libro/crear_libro.html"
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")
    
class ActualizarLibro(UpdateView):
    model=Libro
    form_class = LibroForm
    template_name="libro/crear_libro.html"
    success_url = reverse_lazy("libro:listar_libro")



class EliminarLibro(DeleteView):
    model=Libro
    success_url = reverse_lazy("libro:listar_libro")
    

    def post(self, request,pk,*args,**kwargs):
        object=Libro.objects.get(id = pk)
        object.estado=False
        object.save()

        return redirect('libro:listar_libro')

    
