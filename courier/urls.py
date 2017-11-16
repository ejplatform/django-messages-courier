# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Notification/~create/$",
        view=views.NotificationCreateView.as_view(),
        name='Notification_create',
    ),
    url(
        regex="^Notification/(?P<pk>\d+)/~delete/$",
        view=views.NotificationDeleteView.as_view(),
        name='Notification_delete',
    ),
    url(
        regex="^Notification/(?P<pk>\d+)/$",
        view=views.NotificationDetailView.as_view(),
        name='Notification_detail',
    ),
    url(
        regex="^Notification/(?P<pk>\d+)/~update/$",
        view=views.NotificationUpdateView.as_view(),
        name='Notification_update',
    ),
    url(
        regex="^Notification/$",
        view=views.NotificationListView.as_view(),
        name='Notification_list',
    ),
]
