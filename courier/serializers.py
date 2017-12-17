from django.contrib.auth import get_user_model

from rest_framework import routers, serializers, viewsets

from .models import Notification, UserNotification


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        exclude = ('recipients',)


class UserNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()

    class Meta:
        model = UserNotification
        exclude = ('user',)