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
from courier.emails.providers.onesignal.models import OneSignalEmailProfile
from courier.emails.providers.onesignal.serializers import UserTagsSerializer

User = get_user_model()

app_id = settings.COURIER_ONESIGNAL_APP_ID
api_key = settings.COURIER_ONESIGNAL_USER_ID

def get_users(page, limit=300):
    params = {
        'headers': {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Basic {}'.format(api_key)
        }
    }

    params['url'] = 'https://onesignal.com/api/v1/players?app_id={}&limit=300&offset={}' \
        .format(app_id, str(page*limit))

    return requests.get(**params)


def get_all_users(pages):
    data = []
    for page in range(pages):
        r = get_users(page)
        d = json.loads(r.content)
        data += d['players']

    return data

def get_email_auth_hash(onesignal_api_key, email_address):
    hmac_o = hmac.new(onesignal_api_key.encode(), digestmod='sha256')
    hmac_o.update(email_address.encode())
    return hmac_o.hexdigest()


class Command(BaseCommand):
    help = 'Export users data in a csv file'

    def handle(self, *files, **options):
        r = get_users(0, 1)
        if r.status_code == 200:
            total = json.loads(r.content)['total_count']
            pages = int(total / 300) + 1
        else:
            raise ConnectionError

        data = get_all_users(pages)
        onesignal_emails = {}
        for u in data:
            try:
                validate_email(u['identifier'])
                onesignal_emails[u['identifier']] = {
                    'id' : u['id']
                }
            except:
                pass

        local_emails = []
        local_emails += EmailProfile.objects\
            .values_list('user__email', flat=True)
        local_emails += NotificationProfile.objects\
            .values_list('user__email', flat=True)
        local_emails = set(local_emails)
        players_to_create = [le for le in local_emails
                             if not(le in onesignal_emails.keys())]

        counter = 0
        for player in players_to_create:
            counter+=1
            if counter % 100 == 0:
                print(player, ': ', counter)
            email_auth_hash = get_email_auth_hash(api_key, player)
            user = User.objects.get(email=player)
            requests_params = {
                'url': "https://onesignal.com/api/v1/players",
                'headers': {
                    "Content-Type": "application/json"
                },
                'data': json.dumps({
                    'app_id': app_id,
                    'device_type': 11,
                    'identifier': player,
                    'email_auth_hash': email_auth_hash,
                    'tags': UserTagsSerializer(user).data
                })
            }

            r = requests.post(**requests_params)
            result = json.loads(r.content)
            if r.status_code == 200 and result['success']:
                try:
                    profile = OneSignalEmailProfile(
                        user=User.objects.get(email=player),
                        onesignal_id=result['id'])
                    profile.save()
                except:
                    print(player, result)
            else:
                print(r.status_code, player, result)


        for email in onesignal_emails.keys():
            try:
                osep = OneSignalEmailProfile.objects.get(user__email=email)
            except:
                user = User.objects.get(email=email)
                osep = OneSignalEmailProfile()
                osep.user = user
                osep.onesignal_id = onesignal_emails['email']['id']
                print('ERROR: ', email, onesignal_emails[email])




