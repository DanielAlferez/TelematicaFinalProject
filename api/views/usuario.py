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
class UsuarioViewSet(ViewSet):
     def list(self,request,pk=None):
        email = request.user.email_usuario
        if email:
            usuario = Usuario.objects.filter(email_usuario=email)
            if usuario.count() > 0:
                serializer = SimpleUsuarioSerializer(usuario,many=True)
                return Response({'data':serializer.data},status=status.HTTP_200_OK)
            return Response({'message':'El email no se encuentra en uso'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'campos requeridos: email'}, status=status.HTTP_400_BAD_REQUEST) 

     def delete(self,request,pk=None):
        data_keys = request.data.keys()
        email = request.user.email_usuario

        if('password' in data_keys):
            try:
                usuario = Usuario.objects.get(email_usuario=email)
                if usuario.check_password(request.data.get('password')):
                    usuario.delete()

                    return Response({'message':'Se eliminó la informacion correctamente'}, status=status.HTTP_200_OK)
                return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
            except Usuario.DoesNotExist:
                return Response({'message':'El email no se encuentra en uso'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Campo requerido: password'}, status=status.HTTP_400_BAD_REQUEST)
     
     def update(self, request, pk=None):
        data_keys = request.data.keys()
        if ('password' in data_keys):
            try:

                email = request.user.email_usuario
                
                usuario = Usuario.objects.get(email_usuario=email)
                if not usuario.check_password(request.data.get('password')):
                    return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

                #usuario.set_password(request.data.get('password'))
                if('nombres' in data_keys):
                    usuario.nombres_persona = request.data.get('nombres')
                if('apellidos' in data_keys):
                    usuario.apellidos_persona = request.data.get('apellidos')
                if('telefono' in data_keys):
                    usuario.telefono_persona = request.data.get('telefono')
                if('email' in data_keys):
                    usuario.email_persona = request.data.get('email')
                if('texto' in data_keys):
                    key = generate_key(request.data.get('password'))                
                    texto = encrypt_message(request.data.get('texto'),key)
                    usuario.texto = texto
                    usuario.cedula_persona = request.data.get('cedula')

                usuario.save()


                return Response({'message':'Se actualizo informacion correctamente'}, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'message':'El email no se encuentra en uso'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'campos requeridos: PASSWORD ACTUAL'}, status=status.HTTP_400_BAD_REQUEST)
            