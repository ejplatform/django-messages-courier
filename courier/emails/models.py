from django.db import models
from django.conf import settings

class EmailProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='mailing_profile',
        on_delete=models.PROTECT,
        unique=True
    )

    active = models.BooleanField(
        default=False
    )
