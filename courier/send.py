from django.conf import settings
from .models import Notification, UserNotification
from .pushnotifications.providers.onesignal.provider import send as send_onesignal



def send(title, message, recipients, sender='', provider=None):

    if not provider:
        if not settings.COURIER_DEFAULT_PROVIDER:
            print('Provedor nao colocado')
            raise NotImplementedError

    if settings.COURIER_DEFAULT_PROVIDER != 'onesignal':
        print('provedor nao é onesignal')
        raise NotImplementedError

    # First let's save the notification in the DB, then let's send it
    n = Notification(sender=sender, title=title, short_description=message)
    n.save()

    for user in recipients:
        UserNotification.objects.create(user=user, notification=n)

    send_onesignal(title, message, recipients, sender)

