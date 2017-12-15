from rest_framework.routers import SimpleRouter
from .views import NotificationProfileViewSet


router = SimpleRouter()
router.register(r'profile', NotificationProfileViewSet, base_name='notification_profile')

urlpatterns = router.urls

