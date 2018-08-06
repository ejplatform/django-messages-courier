# -*- coding: utf-8 -*-
import json
import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from courier.emails.providers.onesignal.serializers import UserTagsSerializer
from courier.emails.providers.onesignal.management.commands.sync_email_profiles import \
    get_email_auth_hash
from courier.emails.providers.onesignal.models import OneSignalEmailProfile
from ocupa.users.models import User

@receiver(post_save, sender=User, dispatch_uid='update_onesignal_user')
def update_user_tags(sender, instance, **kwargs):
    if instance.onesignal_email_info.exists():
        url = 'https://onesignal.com/api/v1/players/{}'\
            .format(instance.onesignal_email_info.first().onesignal_id)
    else:
        url = 'https://onesignal.com/api/v1/players'
    email_auth_hash = get_email_auth_hash(settings.COURIER_ONESIGNAL_USER_ID,
                                          instance.email)
    requests_params = {
        'url': url,
        'headers': {
            "Content-Type": "application/json"
        },
        'data': json.dumps({
            'app_id': settings.COURIER_ONESIGNAL_APP_ID,
            'device_type': 11,
            'identifier': instance.email,
            'email_auth_hash': email_auth_hash,
            'tags': UserTagsSerializer(instance).data
        })
    }

    if instance.onesignal_email_info.exists():
        r = requests.put(**requests_params)
    else:
        r = requests.post(**requests_params)
    result = json.loads(r.content)
    if r.status_code == 200 and result['success']:
        try:
            profile = OneSignalEmailProfile(
                user=User.objects.get(email=instance.email),
                onesignal_id=result['id'])
            profile.save()
        except:
            print(instance.email, result)
    else:
        print(r.status_code, instance.email, result)

