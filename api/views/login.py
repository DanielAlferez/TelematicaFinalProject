from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models.usuario import Usuario

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class LoginViewSet(ViewSet):
    def create(self, request):
        if 'email' in request.POST and 'password' in request.POST:
            try:
                usuario = Usuario.objects.get(email_usuario=request.POST['email'])
                
                if usuario.check_password(request.POST['password']):
                    tokens = RefreshToken.for_user(usuario)  # Corrección aquí
                    return Response({
                        'tokens': {
                            'accessToken': str(tokens.access_token),
                            'refreshToken': str(tokens)
                        },
                        'email': usuario.email_usuario,
                        'rol': usuario.rol_usuario,
                        'nombres': usuario.nombres_persona,
                        'apellidos': usuario.apellidos_persona
                    })
                else:
                    return Response({'message': 'usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
            except Usuario.DoesNotExist: 
                return Response({'message': 'usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'campos requeridos: email, password'}, status=status.HTTP_400_BAD_REQUEST)
