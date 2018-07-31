# -*- coding: utf-8 -*-
import json
import hmac
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

from courier.emails.models import EmailProfile
from courier.pushnotifications.providers.onesignal.models import NotificationProfile

User = get_user_model()

app_id = settings.COURIER_ONESIGNAL_APP_ID
api_key = settings.COURIER_ONESIGNAL_USER_ID

def update_user(player_id, tags):
    params = {
        'headers': {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Basic {}'.format(api_key)
        },
        'data': json.dumps({
            'app_id': app_id,
            'tags': tags,
            'email_auth_hash': get_email_auth_hash(api_key, 'virgilio.santos@gmail.com')
        })
    }

    print(params)

    params['url'] = 'https://onesignal.com/api/v1/players/{}' \
        .format(player_id)

    return requests.put(**params)


def get_email_auth_hash(onesignal_api_key, email_address):
    hmac_o = hmac.new(onesignal_api_key.encode(), digestmod='sha256')
    hmac_o.update(email_address.encode())
    return hmac_o.hexdigest()


class Command(BaseCommand):
    help = 'Add tags to all users'

    def handle(self, *args, **options):
        player_id = '23cbc583-bb52-4b26-93e0-ee3eb7cf31bf'
        r = update_user(player_id, tags={'gender': 'Male', 'state': 'Bahia', 'birth_date': '06/02/1986'})
        if r.status_code == 200:
            print(r.content)
        else:
            print(r.status_code, r.content)
        #     try:
        #         np = NotificationProfile.objects.get(user__email=email)
        #         print(np.onesignal_id, onesignal_emails[email])
        #     except:
        #         print('ERROR: ', email, onesignal_emails[email])



