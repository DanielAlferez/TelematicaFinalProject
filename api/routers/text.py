from api.views.text import TextViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TextViewSet, basename='texto')
urlpatterns = router.urls
