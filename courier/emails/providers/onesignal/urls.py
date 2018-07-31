from rest_framework.routers import SimpleRouter
from .views import OneSignalEmailProfileViewSet


router = SimpleRouter()
router.register(r'profile', OneSignalEmailProfileViewSet, base_name='onesignal_email_profile')

urlpatterns = router.urls

