from django.urls import path, include
from api.routers import usuarios
from api.routers import login
from api.routers import text
from api.routers import all_usuarios
from api.routers import usuario
urlpatterns = [
    
    path(r'usuarios/', include(usuarios.router.urls)),
    path(r'usuarios/all', include(all_usuarios.router.urls)),
    path(r'login/', include(login.router.urls)),
    path(r'usuario/', include(usuario.router.urls)),
    path(r'texto/', include(text.router.urls)),

]