from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.viewsets import ViewSet

from api.models.usuario import Usuario

from api.utils.encrypt import encrypt_message, decrypt_message, generate_key
from api.serializers.simple_user_serializer import SimpleUsuarioSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class TextViewSet(ViewSet):
    def create(self, request):
        data_keys = request.data.keys()
        email = request.user.email_usuario
        
        if ('password' in data_keys):
            usuario = Usuario.objects.get(email_usuario=email)
            if usuario.check_password(request.POST['password']):
                
                key = generate_key(request.POST['password'])
                texto = decrypt_message(usuario.texto,key)                

                return Response({'Texto': texto}, status=status.HTTP_200_OK)
            return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
            
            
        return Response({'message': 'Campo requerido: password'}, status=status.HTTP_400_BAD_REQUEST)

   