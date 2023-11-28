from django.contrib.gis.admin import GeoModelAdmin
from django.contrib import admin
from .models import MySpatialModel


# Register your models here.
@admin.register(MySpatialModel)
class MySpatialModelAdmin(GeoModelAdmin):
    # GeoModelAdmin offers additional functionality in the admin for viewing and editing geospatial fields
    pass
