from django.db import models
from django.contrib.auth.models import BaseUserManager

class AdministradorUsuario(BaseUserManager):
    def _create_user(self,cedula_persona,nombres_persona,apellidos_persona,telefono_persona, email_usuario,texto, password=None):
        if not email_usuario:
            raise ValueError('El usuario debe proporcionar un email')
        if password:
            usuario = self.model(email_usuario=self.normalize_email(email_usuario))
            usuario.cedula_persona = cedula_persona
            usuario.nombres_persona = nombres_persona
            usuario.apellidos_persona = apellidos_persona
            usuario.telefono_persona = telefono_persona
            usuario.texto = texto
            usuario.rol_usuario = 'user'
            usuario.set_password(password)
            usuario.save(using=self.db)
            return usuario
        else:
            raise ValueError('La contraseña no debe estar vacía')
        
    def _create_superuser(self,cedula_persona,nombres_persona,apellidos_persona,telefono_persona, email_usuario,texto, password=None):
        if not email_usuario:
            raise ValueError('El usuario debe proporcionar un email')
        if password:
            usuario = self.model(email_usuario=self.normalize_email(email_usuario))
            usuario.cedula_persona = cedula_persona
            usuario.nombres_persona = nombres_persona
            usuario.apellidos_persona = apellidos_persona
            usuario.telefono_persona = telefono_persona
            usuario.texto = texto
            usuario.rol_usuario = 'admin'
            usuario.set_password(password)
            usuario.save(using=self.db)
            return usuario
        else:
            raise ValueError('La contraseña no debe estar vacía')

    def create_user(self, email_usuario, password=None):
        if not email_usuario:
            raise ValueError('El usuario debe proporcionar un email')
        if password:
            usuario = self.model(email_usuario=self.normalize_email(email_usuario))
            usuario.rol_usuario = 'user'
            usuario.set_password(password)
            usuario.save(using=self.db)
            return usuario
        else:
            raise ValueError('La contrasenna no debe estar vacia')

    def create_superuser(self, email_usuario, password=None):
        if not email_usuario:
            raise ValueError('El usuario debe proporcionar un email')
        if password:
            usuario = self.model(email_usuario=self.normalize_email(email_usuario))
            usuario.rol_usuario = 'admin'
            usuario.set_password(password)
            usuario.save(using=self.db)
            return usuario
        else:
            raise ValueError('La contrasenna no debe estar vacia')