import requests
from django.conf import settings
from .models import OneSignalEmailProfile



def send(title, message, recipients, sender=''):
    if not settings.COURIER_ONESIGNAL_ID:
        raise NameError

    list_of_ids = []
    for user in recipients:
        list_of_ids.append(OneSignalEmailProfile.objects.get(user=user).onesignal_id)

    if type(title) == str:
        title = {'en': title}

    if type(message) == str:
        message = {'en': message}

    request_dict = {
        'include_player_ids': list_of_ids,
        'app_id': settings.COURIER_ONESIGNAL_APP_ID,
        'contents': message,
        'headings': title
    }

    request_headers = {
        'Authorization': 'Basic {}'.format(settings.COURIER_ONESIGNAL_USER_ID)
    }
    r = requests.post('https://onesignal.com/api/v1/notifications', json=request_dict, headers=request_headers)

    return r.status_code
