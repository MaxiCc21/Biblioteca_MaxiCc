from django.shortcuts import redirect, render
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import  LoginRequiredMixin

from .models import *
from .forms import UserForm
from .mixins import SuperUserRequireMixin

# Create your views here.


class Inicio(LoginRequiredMixin,TemplateView):
    template_name="index.html"
 

class ListarUsuario_ListView(LoginRequiredMixin,SuperUserRequireMixin,ListView):
    model = User
    template_name= 'usuario/listar_usuario.html'
    
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["usuarios"] = self.get_queryset()
        return contexto

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())



class CrearUsuario_CreateView(LoginRequiredMixin,SuperUserRequireMixin,CreateView):
    model = User
    form_class = UserForm
    template_name='usuario/registrar_usuario.html'

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["form"] = self.form_class
        return contexto

    def get(self, request,*args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = User(
                email = form.cleaned_data.get('email'),
                username= form.cleaned_data.get('username'),
                name = form.cleaned_data.get('name'),
                last_name = form.cleaned_data.get('last_name')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('login:listar_usuario')
        else:
            return render(request,self.template_name,{'form':form})


class ActualizarUsuario_UpdateView(LoginRequiredMixin,SuperUserRequireMixin,UpdateView):
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
    
class EliminarUsuario_DeleteView(LoginRequiredMixin,SuperUserRequireMixin,DeleteView):
    model = User
    template_name = "usuario/eliminar_usuario.html"

    def post(self, request,pk,*args,**kwargs):
        object=self.model.objects.get(id = pk)
        object.active_user=False
        object.save()

        return redirect('login:listar_usuario')


    

    


