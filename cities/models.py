from uuid import uuid4
from django.db import models
from django.contrib import admin
from django.contrib.gis.db import models as geomodels


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = geomodels.PointField()
    state_id = models.CharField(max_length=2)
    county_fips = models.IntegerField()
    county_name = models.CharField(max_length=255)
    population = models.IntegerField()
    density = models.IntegerField()
    military = models.BooleanField()
    incorporated = models.BooleanField()
    timezone = models.CharField(max_length=255)
    ranking = models.IntegerField()
    zips = models.CharField(max_length=255)


admin.site.register(City)
