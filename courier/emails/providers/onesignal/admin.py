from django.contrib import admin
from .models import OneSignalEmailProfile


class NotificationProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'onesignal_id',  'created', 'modified',]
    list_display = ['user', 'onesignal_id',  'created', 'modified',]
    search_fields = ['user__username', 'user__email', 'onesignal_id',]
    readonly_fields = ['created', 'modified',]


admin.site.register(OneSignalEmailProfile, NotificationProfileAdmin)
