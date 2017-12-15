from rest_framework import serializers

from .models import NotificationProfile


class NotificationProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = NotificationProfile
        fields = ('user', 'onesignal_id',)
