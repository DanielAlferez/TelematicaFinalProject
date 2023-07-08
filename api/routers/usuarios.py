from api.views.usuarios import UsuariosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsuariosViewSet, basename='usuario')
urlpatterns = router.urls
