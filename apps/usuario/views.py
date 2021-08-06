from django.shortcuts import redirect, render
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import UserForm

# Create your views here.



class ListarUsuario_ListView(ListView):
    model = User
    template_name= 'usuario/listar_usuario.html'
    
    def get_queryset(self):
        return self.model.objects.filter(active_user=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["usuarios"] = self.get_queryset()
        return contexto

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())



class CrearUsuario_CreateView(CreateView):
    form_class = UserForm
    template_name='usuario/registrar_usuario.html'

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
            return redirect("login:listar_usuario")
        else:
            ValueError


class ActualizarUsuario_UpdateView(UpdateView):
    model=User
    form_class = UserForm
    template_name= 'usuario/editar_usuario.html'
    success_url = reverse_lazy("login:listar_usuario")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context["object"] = self.get_object()
        context["usuario"] = self.model.objects.filter(active_user=True)
        return context
    
class EliminarUsuario_DeleteView(DeleteView):
    model = User
    template_name = "usuario/eliminar_usuario.html"

    def post(self, request,pk,*args,**kwargs):
        object=self.model.objects.get(id = pk)
        object.active_user=False
        object.save()

        return redirect('login:listar_usuario')


    

    


