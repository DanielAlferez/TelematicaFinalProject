from api.views.usuario import UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsuarioViewSet, basename='usuario')
urlpatterns = router.urls
