# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
    Notification,
)


class NotificationCreateView(CreateView):

    model = Notification


class NotificationDeleteView(DeleteView):

    model = Notification


class NotificationDetailView(DetailView):

    model = Notification


class NotificationUpdateView(UpdateView):

    model = Notification


class NotificationListView(ListView):

    model = Notification
