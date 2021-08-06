from django.shortcuts import redirect, render
from django.views.generic import View,TemplateView,ListView,CreateView,DeleteView

from apps.usuario.models import *
from .forms import UserForm

# Create your views here.



class ListarUsuario_ListView(ListView):
    model = User
    template_name= 'usuario/listar_usuario.html'
    
    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["usuarios"] = self.get_queryset()
        return contexto

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context=self.get_context_data())



class CrearUsuario_CreateView(CreateView):
    form_class = UserForm
    template_name = "usuario/registrar_usuario.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["form"] = self.form_class
        return context

    def get(self, request, *args,**kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect("usuario/listar_usuario.html")