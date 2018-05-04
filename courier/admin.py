from django.contrib import admin
from django.conf import settings
import requests

from courier.emails.models import EmailProfile
from .forms import NotificationSendInBulkForm
from django.template.response import TemplateResponse
from django.conf.urls import url
from .models import Notification, UserNotification
from django.contrib.auth import get_user_model


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['sender', 'title', 'created', 'modified',]
    search_fields = ['sender', 'title', 'short_description', 'recipients',]
    readonly_fields = ['created', 'modified',]
    change_list_template = 'admin/notification_with_bulk_send_button.html'

    def bulk_send(self, request):
        if request.method == 'POST':
            form = NotificationSendInBulkForm(request.POST)
            if form.is_valid():
                # If form is valid, all users have the notification on their models
                # and a notification is sent.
                notification = Notification.objects.create(**form.cleaned_data)
                all_user_notifications = [UserNotification(user=user, notification=notification) for user in get_user_model().objects.all()]
                UserNotification.objects.bulk_create(all_user_notifications)

                request_dict = {
                    'app_id': settings.COURIER_ONESIGNAL_APP_ID,
                    'contents': {'en': form['short_description'].data},
                    'headings': {'en': form['title'].data},
                    'included_segments': ['All', ]
                }

                request_headers = {
                    'Authorization': 'Basic {}'.format(settings.COURIER_ONESIGNAL_USER_ID)
                }
                r = requests.post('https://onesignal.com/api/v1/notifications', json=request_dict, headers=request_headers)

                context = self.admin_site.each_context(request)
                context['opts'] = self.model._meta
                return TemplateResponse(request, 'admin/notification_bulk_send_result.html', context)
        else:
            form = NotificationSendInBulkForm()
            context = self.admin_site.each_context(request)
            context['opts'] = self.model._meta
            context['form'] = form
            return TemplateResponse(request, 'admin/notification_bulk_send.html', context)

    def get_urls(self):
        urls = super(NotificationAdmin, self).get_urls()
        my_urls = [url(r"^bulk-send/$", self.bulk_send, name='bulk-notification-send'), ]

        return my_urls+urls


class UserNotificationAdmin(admin.ModelAdmin):
    fields = ['user', 'notification', 'status', 'created', 'modified',]
    list_display = ['user', 'notification', 'status', 'created', 'modified',]
    search_fields = ['user__username', 'user__email', 'status']
    readonly_fields = ['created', 'modified',]


class EmailProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'active']

admin.site.register(Notification, NotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
admin.site.register(EmailProfile, EmailProfileAdmin)
