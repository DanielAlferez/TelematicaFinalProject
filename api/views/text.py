from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.viewsets import ViewSet

from api.models.usuario import Usuario
from api.utils.send_email import send
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
    
    def update(self, request, pk=None):
        data_keys = request.data.keys()
        email = request.user.email_usuario
        if('password' in data_keys,
           'password_new' in data_keys):
            usuario = Usuario.objects.get(email_usuario=email) 
            if usuario.check_password(request.data.get('password')):
                key_old = generate_key(request.data.get('password'))
                texto_old = decrypt_message(usuario.texto,key_old)                
                

                key = generate_key(request.data.get('password_new'))
                texto = encrypt_message(texto_old,key)

                usuario.texto = texto
                usuario.set_password(request.data.get('password_new'))
                usuario.save()
                cuerpo = "Se ha modificado la contraseña correctamente!\nSu nueva contraseña es: " + request.data.get('password_new')
                send(usuario.email_usuario,"Modificación de contraseña",cuerpo)
                return Response({'message': 'Contraseña actualizada corectamente'}, status=status.HTTP_200_OK)

            return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
            
   