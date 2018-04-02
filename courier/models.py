# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Notification(TimeStampedModel):
    sender = models.CharField(_('Sender'), max_length=50)
    title = models.CharField(_('Title'), max_length=200)
    short_description = models.TextField(
        _('Short Description'),
        blank=True,
    )
    recipients = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='UserNotification',
    )


class UserNotification(TimeStampedModel):
    STATUS_WAITING = 'waiting'
    STATUS_READ = 'read'
    STATUS_SEEN = 'seen'
    STATUS_UNSEEN = 'unseen'
    STATUS_CHOICES = (
        (STATUS_WAITING, _('Waiting')),
        (STATUS_READ, _('Read')),
        (STATUS_SEEN, _('Seen')),
        (STATUS_UNSEEN, _('Unseen')),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_notifications',
        on_delete=models.PROTECT,
    )
    notification = models.ForeignKey(
        Notification,
        related_name='user_notifications',
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        _('Status'),
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_WAITING,
    )

    class Meta:
        unique_together = [('user', 'notification')]
