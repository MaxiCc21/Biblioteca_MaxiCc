from django import forms
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        label = {
            'nombre' : 'Nombre del autor',
            'apellido' : 'Apelldio del autor',
            'nacionalidad' : 'Nacionalidad del autor',
            'descripcion' : 'Descipcion'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del autor',
                    'id': 'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellidos del autor',
                    'id': 'apellidos'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad del autor',
                    'id': 'nacionalidad'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'id': 'descripcion'
                }
            )
        }



class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','autor_id','fecha_publicacion',]
        label = {
            'titulo' : 'Titulo del autor',
            'autor_id' : 'Nombre de los autores',
            'fecha_publicacion' : 'Fecha de publicacion',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el titulo del libro',
                    'id': 'titulo'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'style': 'height:100px'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top:5px'
                }
            ),
        }
