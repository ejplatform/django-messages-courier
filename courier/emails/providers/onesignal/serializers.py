from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import OneSignalEmailProfile


class OneSignalEmailProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = OneSignalEmailProfile
        fields = ('user', 'onesignal_id', )



class UserTagsSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = get_user_model()
        fields = ('state', 'last_login', )
