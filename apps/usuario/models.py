from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager, PermissionsMixin
# Create your models here.

class User_Manager(BaseUserManager):
    def create_user(self,email,username,name,last_name,password = None):
        if not email:
            raise ValueError("El usuario debe tener un correo electronico")
        
        user =self.model(
            username = username,
            email = self.normalize_email(email),
            name=name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,name,last_name,password = None):
        user = self.create_user(
            email,
            username=username,
            name=name,
            last_name=last_name,
            password=password,
        )
        user.administator = True
        user.save()
        return user
class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key = True)
    username = models.CharField("Nombre de usuario", max_length=100,unique=True)
    email = models.EmailField("Correo electronico", max_length=150,unique=True)
    name = models.CharField("Nombre", max_length=200,blank=True,null=True)
    last_name = models.CharField("Apellido", max_length=50)
    image = models.ImageField("Imagen de perfil",max_length=None, upload_to="perfil/", height_field=None,width_field=None,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = User_Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email','name','last_name']

    def __str__(self):
        return ("{0}, {1}").format(self.name,self.last_name)

