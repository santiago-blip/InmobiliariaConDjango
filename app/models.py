from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,nombre,apellido,password = None):
        if not email:
            raise ValueError("El usuario debe tener email")
        
        usuario = self.model(nombre = nombre,apellido = apellido,email = email)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,nombre,apellido,email,password):
        usuario = self.create_user(email,nombre = nombre,apellido = apellido,password=password)
        usuario.admin_access = True
        usuario.save()

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroCelular = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='perfil/',height_field=None,width_field=None,max_length=100,blank=True,null=True)
    admin_access = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nombre','apellido']

    def has_perm(self,perm,obj = None):
    	return True

    def has_module_perms(self,app_label):
	    return True

    @property
    def is_staff(self):
	    return self.admin_access
    
    class Meta:
        db_table = 'tbl_usuario'

class Casa(models.Model):
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='casa/',height_field=None,width_field=None,max_length=100)

    class Meta:
        db_table = 'tbl_casa'

class GaleriaCasa(models.Model):
    idCasa = models.ForeignKey(Casa,on_delete=models.CASCADE)
    imagenGaleria = models.ImageField(upload_to='galeria/',height_field=None,width_field=None,max_length=100,blank=True,null=True)