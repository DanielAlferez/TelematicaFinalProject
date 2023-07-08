from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models.usuario import Usuario
from api.serializers.simple_user_serializer import SimpleUsuarioSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated & IsAdminUser])

class UsuariosViewSet(ViewSet):
    def list(self,request,pk=None):
        queryset = Usuario.objects.all()
        serializer = SimpleUsuarioSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
