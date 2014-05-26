#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import patterns, url

from tags import views

urlpatterns = patterns('',
    url(r'^$', views.tag_view, name='tag_view')
)
