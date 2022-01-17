#!/usr/bin/python
# -*- coding:utf-8 -*-

"""定义learning_logs的URL模式"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index')
]
