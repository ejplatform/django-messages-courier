from django.contrib import admin
from django.conf import settings

from .models import Notification, UserNotification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['sender', 'title', 'created', 'modified',]
    search_fields = ['sender', 'title', 'short_description', 'recipients',]
    readonly_fields = ['created', 'modified',]


class UserNotificationAdmin(admin.ModelAdmin):
    fields = ['user', 'notification', 'status', 'created', 'modified',]
    list_display = ['user', 'notification', 'status', 'created', 'modified',]
    search_fields = ['user__username', 'user__email', 'status']
    readonly_fields = ['created', 'modified',]


admin.site.register(Notification, NotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
