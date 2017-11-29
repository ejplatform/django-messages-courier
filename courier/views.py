from rest_framework import viewsets, permissions

from .models import Notification, UserNotification
from .serializers import NotificationSerializer, UserNotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserNotificationViewSet(viewsets.ModelViewSet):
    serializer_class = UserNotificationSerializer
    queryset = UserNotification.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
