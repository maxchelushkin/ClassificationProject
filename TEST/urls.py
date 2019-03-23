
from django.conf.urls import url, include
from django.contrib import admin
from raster.views import AlgebraView, ExportView, LegendView
from testApp.views import index
import shapeEditor.tms.urls

urlpatterns = [
    url(r'^tms/', include(shapeEditor.tms.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^raster/tiles/layer_id/{z}/{x}/{y}.tif', include('raster.urls')),
    url(r'/raster/tiles/layer_id/{z}/{x}/{y}.tif', AlgebraView.as_view()),
    url(r'^tiles/(?P<layer>[^/]+)/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+).(?P<frmt>png|jpg|tif)$',
        AlgebraView.as_view(),
        name='tms',
    ),
        Normal raster tiles endpoint
    url(
        r'^tiles/(?P<layer>[^/]+)/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+).(?P<frmt>png|jpg|tif)$',
        AlgebraView.as_view(),
        name='tms',
    ),

    # Raster algebra endpoint
    url(
        r'^algebra/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+).(?P<frmt>jpg|png|tif)$',
        AlgebraView.as_view(),
        name='algebra',
    ),

    # Pixel value endpoint
    url(
        r'^pixel/(?P<xcoord>-?\d+(?:\.\d+)?)/(?P<ycoord>-?\d+(?:\.\d+)?)$',
        AlgebraView.as_view(),
        name='pixel',
    ),

    # Raster legend endpoint
    url(
        r'^legend(?:/(?P<legend_id>[^/]+))?/$',
        LegendView.as_view(),
        name='legend',
    ),

    # Exporter endpoint
    url(
        r'^export$',
        ExportView.as_view(),
        name='export',
    ),
]
