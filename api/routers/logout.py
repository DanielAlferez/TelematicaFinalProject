from api.views.logout import LogoutViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', LogoutViewSet, basename='logout')
urlpatterns = router.urls