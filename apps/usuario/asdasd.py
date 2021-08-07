
from django import forms
from apps.usuario.models import User

class UserForm(forms.ModelForm):
    """Formulario de registro de una usuario en la base de datos
    
    Variables:
        - password1: Contraseña
        - password2: Verificacion de contraseña
        
    """
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': "Ingrese contraseña...",
            'id' : "password1",
            'require': 'required',
        }
    ))

    password2 = forms.CharField(label = "Contraseña de confirmacion",widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Confirme contrañes',
            'id' : 'password2',
            'required' : 'required'
        }
    ))

    class Meta:
        model = User
        fields = ("email",'username','name','last_name')
        widgets ={ 
            'email' : forms.EmailInput(
                attrs={
                    'class': 'form-class',
                    'placeholder': "Ingrese su correo electronico",
                    'id':'email',
                    'required' : 'required',
            }
        ),
            "username":forms.TextInput(attrs={
                'class':'form-class',
                'placeholder':'Ingrese nombre de usuario',
                'id':'username',
                'required':'required'
            }
        ),
            'name': forms.TextInput(attrs=
            {
                'class':'form-class',
                'placeholder':"Ingrese su nombre",
                'id':'name',
                'required':'required'
            }
        ),
            'last_name':forms.TextInput(attrs=
            {
                'class': 'form-class',
                "placeholder": 'ingrese su apellido',
                'id' : 'last_name',
                'required':'required',
            }
        ),
                }

        def clean_password2(self):
            """Vlidacion de contrseña
            
            Metodo que valida que ambas contraseñas ingresadas sean iguales, esto antes de ser encriptadas

            Excepcion:
                -validationError -- cuando las contraseñas no son iguales entre si
            """

            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("La contraseña no coincide")
            return password2

        def save(self,commit = True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
            return user