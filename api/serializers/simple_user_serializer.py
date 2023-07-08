from rest_framework import serializers
from api.models.usuario import Usuario

#Usuario Model
class SimpleUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('cedula_persona','nombres_persona','apellidos_persona','email_usuario','texto')