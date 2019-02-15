from wms import maps, layers, views

# Load model with spatial field (Point, Polygon, MultiPolygon)
from cities.models import City

class MyWmsLayer(layers.WmsVectorLayer):
    model = City

class MyWmsMap(maps.WmsMap):
    layer_classes = [ MyWmsLayer ]

class MyWmsView(views.WmsView):
    map_class = MyWmsMap