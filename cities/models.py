from uuid import uuid4
from django.db import models
from django.contrib import admin


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    state_id = models.CharField(max_length=2)
    county_fips = models.IntegerField()
    county_name = models.CharField(max_length=255)
    population = models.IntegerField()
    density = models.IntegerField()
    military = models.BooleanField()
    incorporated = models.BooleanField()
    timezone = models.CharField(max_length=255)
    ranking = models.IntegerField()
    zips = models.CharField(max_length=2000)
    average_wages_and_salaries = models.IntegerField(
        help_text="Average wages and salaries in dollars"
    )
    per_capita_dividends_interest_and_rent = models.IntegerField(
        help_text="Per capita dividends, interest, and rent in dollars"
    )
    per_capita_net_earnings = models.IntegerField(
        help_text="Per capita net earnings in dollars"
    )
    per_capita_personal_income = models.IntegerField(
        help_text="Per capita personal income in dollars"
    )
    total_employment = models.IntegerField(
        help_text="Total Full-Time and Part-Time Employment by NAICS Industry in number of jobs"
    )


admin.site.register(City)
