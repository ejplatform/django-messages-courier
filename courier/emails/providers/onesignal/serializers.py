from django.contrib.auth import get_user_model
from rest_framework import serializers

from courier.emails.providers.onesignal.models import OneSignalEmailProfile


class OneSignalEmailProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = OneSignalEmailProfile
        fields = ('user', 'onesignal_id', )



class UserTagsSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(read_only=True, slug_field='name')
    last_login = serializers.SerializerMethodField()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        for key in repr:
            if repr[key] is None:
                repr[key] = ''
        return repr

    class Meta:
        model = get_user_model()
        fields = ('state', 'last_login', 'from_import',)


    def get_last_login(self, obj):
        if obj.last_login:
            return str(obj.last_login.date())
        return obj.last_login
