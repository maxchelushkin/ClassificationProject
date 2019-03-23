"""TEST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from raster.views import AlgebraView, ExportView, LegendView
from testApp.views import index
from shapeEditor.tms.views import *

urlpatterns = [
    url(r'^$', root),
    url(r'^(?P<version>[0-9.]+)$', service)
    url(r'^(?P<version>[0-9.]+)/(?P<shapefile_id>\d+)$', tileMap)
    url(r'^(?P<version>[0-9.]+)/(?P<shapefile_id>\d+)/(?P<zoom>\d+)/(?P<x>\d+)/(?P<y>\d+)\.tif$', tile)
]
