from rest_framework import serializers

from .models import EmailProfile


class EmailProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = EmailProfile
        fields = ('user', 'active',)
