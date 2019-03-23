from django.contrib.gis.gdal import GDALRaster
from datetime import datetime
# from testApp.models import RasterLayer
from django.utils import timezone
import pytz
from raster.models import RasterLayer
import os
from osgeo import gdal

file = 'test.tif'
path = "/home/maxim/temp/TEST/test.tif"
name = "test.tif"
dem = RasterLayer(rasterfile = file, name = name, datatype = 'co')
dem.save()
