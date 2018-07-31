from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db.models import Count

from courier.emails.models import EmailProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Create missing E-mail profile for all users'

    def handle(self, *args, **options):
        users = User.objects\
            .exclude(from_import=True)\
            .exclude(mailing_profile__isnull=False)
        for u in users:
            ep = EmailProfile()
            ep.user = u
            ep.active = False
            ep.save()

        users = User.objects\
            .filter(from_import=True)\
            .filter(last_login__isnull=False)\
            .exclude(mailing_profile__isnull=False)
        for u in users:
            ep = EmailProfile()
            ep.user = u
            ep.active = False
            ep.save()

        
