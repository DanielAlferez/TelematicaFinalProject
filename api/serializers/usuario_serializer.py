from rest_framework import serializers
from api.models.usuario import Usuario

#Usuario Model
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' 