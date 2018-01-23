from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter
from .views import NotificationViewSet, UserNotificationViewSet


router = SimpleRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'user-notifications', UserNotificationViewSet)

urlpatterns = [
    url(r'^onesignal/', include('courier.pushnotifications.providers.onesignal.urls')),
    url(
        regex=r'^user-notifications/(?P<pk>[0-9]+)/read/$',
        view=UserNotificationViewSet.as_view({'post': 'mark_as_read'}),
        name='user-notifications-read'
    ),
    url(
        regex=r'^user-notifications/(?P<pk>[0-9]+)/unread/$',
        view=UserNotificationViewSet.as_view({'post': 'mark_as_unread'}),
        name='user-notifications-unread'
    ),
] + router.urls
