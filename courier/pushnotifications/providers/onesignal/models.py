from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class NotificationProfile(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='notification_info',
        on_delete=models.CASCADE,
    )
    onesignal_id = models.CharField(
        _('OneSignal Id'),
        max_length=50,
    )
