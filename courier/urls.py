from rest_framework.routers import SimpleRouter
from .views import NotificationViewSet, UserNotificationViewSet

router = SimpleRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'user-notifications', UserNotificationViewSet)

urlpatterns = router.urls
