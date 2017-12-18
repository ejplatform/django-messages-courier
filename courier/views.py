from rest_framework import viewsets, permissions, mixins

from .models import Notification, UserNotification
from .serializers import NotificationSerializer, UserNotificationSerializer
from .permissions import IsOwner


class NotificationViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    Only used for the client to notify that it has received a new notification
    """
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class UserNotificationViewSet(mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    """
    Meant for users do check for notifications and update its 'seen' status.
    No model should be created by this endpoint. Its instances will be created when a new notification is born
    """
    serializer_class = UserNotificationSerializer
    queryset = UserNotification.objects.all()
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


