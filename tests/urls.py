# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from courier.urls import urlpatterns as courier_urls

urlpatterns = [
    url(r'^', include(courier_urls, namespace='courier')),
]
