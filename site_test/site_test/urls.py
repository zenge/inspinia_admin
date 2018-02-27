"""site_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

import views
# from django.contrib.auth.views import login, logout_then_login
# from django.contrib.auth.views import *
import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^account/login/$',  login, {'template_name': 'index_old.html'}),
    # url(r'^login/', login),
    url(r'^login/', auth_views.login),
    # url(r'^logout/', logout_then_login),
    url(r'^logout/', auth_views.logout_then_login),
    # url(r'^account/logout/$', logout_then_login),
    url(r'^$', views.index),
    url(r'^index/$', views.index),

]
