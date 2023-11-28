from django.contrib.gis.db import models


class MySpatialModel(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(srid=4326)  # or models.PolygonField, etc.

    def __str__(self):
        return self.name
