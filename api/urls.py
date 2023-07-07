from django.urls import path, include
from api.routers import usuario
from api.routers import login
from api.routers import logout
urlpatterns = [
    
    path(r'usuario/', include(usuario.router.urls)),
    path(r'login/', include(login.router.urls)),
    
]