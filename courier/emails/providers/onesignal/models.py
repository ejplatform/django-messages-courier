from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class OneSignalEmailProfile(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='onesignal_email_info',
        on_delete=models.CASCADE,
    )
    onesignal_id = models.CharField(
        _('Player ID'),
        max_length=50,
    )
    user_updated_at = models.DateTimeField(_('User updated at'), null=True)
