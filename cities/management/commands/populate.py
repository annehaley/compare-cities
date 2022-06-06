import json
import pandas
from fetch_data import stats
from django.core.management.base import BaseCommand
from cities.models import City


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        City.objects.all().delete()

        cities_df = pandas.read_csv("data/uscities.csv")
        cities_df = cities_df[cities_df["source"] == "shape"]

        bea_datasheets = {
            stat["datasheet"]: dict(json.load(open(stat["datasheet"])))["BEAAPI"][
                "Results"
            ]["Data"]
            for stat in stats
        }
        demographics_datasheet = list(json.load(open("data/demographics.json")))

        def get_named_value_for_county(name, county_fips):
            matches = [
                c["DataValue"]
                for c in bea_datasheets[name]
                if int(c["GeoFips"]) == int(county_fips)
            ]
            return int(matches[0].replace(",", "")) if len(matches) else -1

        for index, city in cities_df.iterrows():
            print("Saving", city["city_ascii"])

            demographics_matches = {
                x["fields"]["race"]: x["fields"]
                for x in demographics_datasheet
                if x["fields"]["city"] == city["city_ascii"]
                and x["fields"]["state_code"] == city["state_id"]
            }
            male_female_ratio = -1
            median_age = -1
            percentage_white = -1
            percentage_black = -1
            percentage_hispanic_latino = -1
            percentage_asian = -1
            percentage_native_american = -1
            if len(demographics_matches.values()) > 0:
                match = list(demographics_matches.values())[0]
                male_female_ratio = (
                    (match["male_population"] / match["female_population"])
                    if "male_population" in match and "female_population" in match
                    else -1
                )
                median_age = match["median_age"] if "median_age" in match else -1
            if "White" in demographics_matches:
                percentage_white = (
                    demographics_matches["White"]["count"]
                    / demographics_matches["White"]["total_population"]
                ) * 100
            if "Black or African-American" in demographics_matches:
                percentage_black = (
                    demographics_matches["Black or African-American"]["count"]
                    / demographics_matches["Black or African-American"][
                        "total_population"
                    ]
                ) * 100
            if "Hispanic or Latino" in demographics_matches:
                percentage_hispanic_latino = (
                    demographics_matches["Hispanic or Latino"]["count"]
                    / demographics_matches["Hispanic or Latino"]["total_population"]
                ) * 100
            if "Asian" in demographics_matches:
                percentage_asian = (
                    demographics_matches["Asian"]["count"]
                    / demographics_matches["Asian"]["total_population"]
                ) * 100
            if "American Indian and Alaska Native" in demographics_matches:
                percentage_native_american = (
                    demographics_matches["American Indian and Alaska Native"]["count"]
                    / demographics_matches["American Indian and Alaska Native"][
                        "total_population"
                    ]
                ) * 100

            City.objects.create(
                name=city["city_ascii"],
                latitude=city["lat"],
                longitude=city["lng"],
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
                median_age=median_age,
                male_female_ratio=male_female_ratio,
                percentage_white=percentage_white,
                percentage_black=percentage_black,
                percentage_hispanic_latino=percentage_hispanic_latino,
                percentage_asian=percentage_asian,
                percentage_native_american=percentage_native_american,
            )
