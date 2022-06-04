import json
import pandas
from fetch_data import stats
from django.core.management.base import BaseCommand
from cities.models import City
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        City.objects.all().delete()

        cities_df = pandas.read_csv("data/uscities.csv")
        cities_df = cities_df[cities_df["source"] == "shape"]

        datasheets = {
            stat["datasheet"]: dict(json.load(open(stat["datasheet"])))["BEAAPI"][
                "Results"
            ]["Data"]
            for stat in stats
        }

        # print(datasheets)

        def get_named_value_for_county(name, county_fips):
            matches = [
                c["DataValue"]
                for c in datasheets[name]
                if int(c["GeoFips"]) == int(county_fips)
            ]
            return int(matches[0].replace(",", "")) if len(matches) else -1

        for index, city in cities_df.iterrows():
            print("Saving", city["city_ascii"])
            City.objects.create(
                name=city["city_ascii"],
                location=Point(city["lat"], city["lng"]),
                state_id=city["state_id"],
                county_fips=city["county_fips"],
                county_name=city["county_name"],
                population=city["population"],
                density=city["density"],
                military=bool(city["military"]),
                incorporated=bool(city["incorporated"]),
                timezone=city["timezone"],
                ranking=city["ranking"],
                zips=city["zips"],
                average_wages_and_salaries=get_named_value_for_county(
                    "data/avg_wage_salaries.json",
                    city["county_fips"],
                ),
                per_capita_dividends_interest_and_rent=get_named_value_for_county(
                    "data/per_capita_dividends_interest_rent.json",
                    city["county_fips"],
                ),
                per_capita_net_earnings=get_named_value_for_county(
                    "data/per_capita_net_earnings.json",
                    city["county_fips"],
                ),
                per_capita_personal_income=get_named_value_for_county(
                    "data/per_capita_personal_income.json",
                    city["county_fips"],
                ),
                total_employment=get_named_value_for_county(
                    "data/total_employment.json",
                    city["county_fips"],
                ),
            )
