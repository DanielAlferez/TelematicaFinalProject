from api.views.login import LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', LoginViewSet, basename='login')
urlpatterns = router.urls