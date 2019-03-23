from django.shortcuts import render
from django.http import HttpResponse

from django.http import Http404
from shapeEditor.shared.models import Shapefile

# Create your views here.

def root(request):
    return HttpResponse("Tile Map Server")

def service(request, version):
    # return HttpResponse("Tile Map Service")
    try:
        if version != "1.0":
            raise
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version = "1.0" encoding="utf-8" ?>')
        xml.append('<TileMapService version="1.0" services="'baseURL + '">')
        xml.append('   <Title>ShapeEditor Tile Map Service' +
                   '</Title>')
        xml.append('    <Abstract></Abstract>')
        xml.append('    <TileMaps')
        for shapefile in Shapefile.objects.all():
            id = str(shapefile.id)
            xml.append('    <TileMap title="' +
                        shapefile.filename + '"')
            xml.append('        src="EPSG:4326"')
            xml.append('        href="'+baseURL + '/' + id '"/>')
        xml.append('    </TileMaps>')
        xml.append('</TileMapService>')
        response = "\n".join(xml)
        return HttpResponse(response, content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")

def tileMap(request, version, shapefile_id):
    return HttpResponse("Tile Map")

def tile(service, version, shapefile_id, zoom, x, y):
    return HttpResponse("Tile")
