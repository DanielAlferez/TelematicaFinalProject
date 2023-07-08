from api.views.all_usuarios import UsuariosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsuariosViewSet, basename='usuarios')
urlpatterns = router.urls
