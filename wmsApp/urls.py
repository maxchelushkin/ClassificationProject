from .config import MyWmsView
from django.urls import path, include

# Add url patterns to setup map services from the view
urlpatterns = [

    # This creates a WMS endpoint
    path(r'^wms/$', MyWmsView.as_view(), name='wms'),

    # This creates a TMS endpoint
    path(r'^tile/(?P<layers>[^/]+)/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)(?P<format>\.jpg|\.png)$',
        MyWmsView.as_view(), name='tms'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('cities/', include('cities.urls')),
    path('admin/', admin.site.urls),
]