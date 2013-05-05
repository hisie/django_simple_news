# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^$', 'new.views.list', name='new_list'),
        url(r'^(?P<id>\d+)-(?P<slug>([\w,-]+))/$', 'new.views.new_detail', name='new_detail'),
    )