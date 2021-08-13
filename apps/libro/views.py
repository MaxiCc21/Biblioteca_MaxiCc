from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import AutorForm, LibroForm
from .models import Autor, Libro
# Create your views here.


class ListadoAutores(View):
    model = Autor
    template_name= 'autor/listar_autor.html'
    
    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["autores"] = self.get_queryset()
        return contexto

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())

class ActualizarAutor(UpdateView):
    model=Autor
    form_class = AutorForm
    template_name= 'autor/editar_autor.html'
    success_url = reverse_lazy("libro:listar_autor")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context["object"] = self.get_object()
        context["autores"] = self.model.objects.filter(estado=True)
        return context
    

class CrearAutor(CreateView):
    form_class = AutorForm
    template_name='autor/crear_autor.html'

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["form"] = self.form_class
        return contexto

    def get(self, request,*args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro:listar_autor")


class EliminarAutor(DeleteView):
    model = Autor
    template_name="autor/eliminar_autor.html"

    def post(self, request,pk,*args,**kwargs):
        object=Autor.objects.get(id = pk)
        object.estado=False
        object.save()

        return redirect('libro:listar_autor')

######################################################################################################################

class ListarLibros(ListView):
    model = Libro
    template_name='libro/listar_libro.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["libros"] = self.get_queryset()

        return contexto

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())

class CrearLibro(CreateView):
    template_name="libro/crear_libro.html"
    form_class = LibroForm

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["form"] = self.form_class
        return contexto

    def get(self, request,*args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro:listar_libro")



    
class ActualizarLibro(UpdateView):
    model=Libro
    form_class = LibroForm
    template_name="libro/editar_libro.html"
    success_url = reverse_lazy("libro:listar_libro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context["object"] = self.get_object()
        context["libros"] = self.model.objects.filter(estado=True)
        return context
    

class EliminarLibro(DeleteView):
    model=Libro
    template_name="libro/eliminar_libro.html"

    def post(self, request,pk,*args,**kwargs):
        object=Libro.objects.get(id = pk)
        object.estado=False
        object.save()

        return redirect('libro:listar_libro')
        


    
