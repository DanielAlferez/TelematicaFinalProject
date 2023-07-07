from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from api.models.administrador import AdministradorUsuario

class Usuario(AbstractBaseUser):
    ROLES_USUARIOS = (('user', 'user'), ('admin', 'admin'),)
    cedula_persona = models.CharField(max_length=30,null=True)
    nombres_persona = models.CharField(max_length=30,null=True)
    apellidos_persona = models.CharField(max_length=30,null=True)
    telefono_persona = models.CharField(max_length=30,null=True)
    email_usuario = models.EmailField( primary_key=True)
    texto = models.TextField(null=True)
    rol_usuario = models.CharField(max_length=13, choices=ROLES_USUARIOS)
    
    
    objects = AdministradorUsuario()
    USERNAME_FIELD = 'email_usuario'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email_usuario

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return True if self.rol_usuario == 'admin' else False 