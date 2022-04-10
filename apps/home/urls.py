# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('index', views.dynamic_dashboard, name='index'),
    path('register-complaint', views.register_complaint, name='register_complaint'),
    path('get-state-data/<str:state>', views.get_state_data),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
