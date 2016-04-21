"""smlb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app import views as app_views  # new
import settings
from app.models import Marques

marques_all = Marques.objects.all()
total = len(marques_all)/10+1 if len(marques_all)%10 != 0 else len(marques_all)/10
marques_list = []
for i in range(2,total+1):
    marques_list.append(url(r'^marques/%s$' % str(i), app_views.marques, name = 'marques'))

urlpatterns = [
    url(r'^$', app_views.home, name = 'home'),
    url(r'^quisommesnous/$', app_views.quisommesnous, name = 'quisommesnous'),
    url(r'^marques/$', app_views.marques, name = 'marques'),
    url(r'^nosforces/$', app_views.nosforces, name = 'nosforces'),
    url(r'^vouscherchez/$', app_views.vouscherchez, name = 'vouscherchez'),
    url(r'^externalisation/$', app_views.externalisation, name = 'externalisation'),
    url(r'^contact/$', app_views.contact, name = 'contact'),
    url(r'^admin/', include(admin.site.urls)),
] + marques_list