from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models.usuario import Usuario
from api.serializers.simple_user_serializer import SimpleUsuarioSerializer
from api.utils.encrypt import encrypt_message,decrypt_message,generate_key

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes

from api.utils.send_email import send

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated & IsAdminUser])

class UsuariosViewSet(ViewSet):
    def list(self,request,pk=None):
        email = request.query_params.get('email')
        if email:
            usuario = Usuario.objects.filter(email_usuario=email)
            if usuario.count() > 0:

                serializer = SimpleUsuarioSerializer(usuario,many=True)
                return Response({'data':serializer.data},status=status.HTTP_200_OK)
            return Response({'message':'El email no se encuentra en uso'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'campos requeridos: email'}, status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,pk=None):
        data_keys = request.data.keys()
        if ('email' in data_keys):
            try:
                usuario = Usuario.objects.get(email_usuario=request.data.get('email'))
                usuario.delete()

                return Response({'message':'Se eliminó la informacion correctamente'}, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'message':'El email no se encuentra en uso'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'campos requeridos: email'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        data_keys = request.data.keys()
        if ('email' in data_keys,
            'nombre' in data_keys,
            'apellido' in data_keys,
            'telefono' in data_keys,
            'cedula' in data_keys
            ):
            try:
                usuario = Usuario.objects.get(email_usuario=request.data.get('email'))


                #usuario.set_password(request.data.get('password'))
                usuario.nombres_persona = request.data.get('nombre')
                usuario.apellidos_persona = request.data.get('apellido')
                usuario.telefono_persona = request.data.get('telefono')
                usuario.email_persona = request.data.get('email')
                
                usuario.cedula_persona = request.data.get('cedula')



                usuario.save()


                return Response({'message':'Se actualizo informacion correctamente'}, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'message':'No se encontro el email original o el email nuevo ya esta en uso'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'campos requeridos: email, apellidos, nombres, telefono, email, texto, cedula'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        data_keys = request.data.keys()
        
        if ('email' in data_keys,
            'password' in data_keys,
            'nombre' in data_keys,
            'apellido' in data_keys,
            'telefono' in data_keys,
            'texto' in data_keys,
            'cedula' in data_keys,
            ):
            #se registra el usuario
            try:
                Usuario.objects.get(email_usuario=request.POST['email'])
                return Response({'message':'El email ya se encuentra en uso'}, status=status.HTTP_409_CONFLICT)
            except Usuario.DoesNotExist:
                texto = request.POST['texto']
                key = generate_key(request.POST['password'])
                
                texto = encrypt_message(texto,key)

                

                usuario = Usuario.objects._create_user(
                    cedula_persona=request.POST['cedula'],
                    nombres_persona=request.POST['nombre'],
                    apellidos_persona=request.POST['apellido'],
                    telefono_persona=request.POST['telefono'],
                    email_usuario=request.POST['email'], 
                    texto=texto,
                    password=request.POST['password'])
                #se registra los datos personales

                send(usuario.email_usuario,"Bienvenido a nuestra app!","Has sido registrado exitosamente en nuestra app, exitos!")
                serializer = {
                    'email' : usuario.email_usuario,
                    'nombres' : usuario.nombres_persona,
                    'apellidos': usuario.apellidos_persona,
                    'telefono': usuario.telefono_persona,
                    'cedula': usuario.cedula_persona,
                    'texto': usuario.texto
                }

                return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'campos requeridos: email, password, name, lastname, phone'}, status=status.HTTP_400_BAD_REQUEST)