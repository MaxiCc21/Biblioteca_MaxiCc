from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import DeleteView
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DetailView
from django.urls import reverse_lazy
# Create your views here.

"""
    dispatch: valida la patecion y elige el metodo http se utilizo para la solicutud
    http_method_not_allowed(): retorna un error cuado se utiliza un metodo http no soportado o definido
    options():

"""


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



def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})




def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})









def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request,'libro/listar_autor.html',{'autores':autores})

