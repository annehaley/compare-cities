# Uses https://simplemaps.com/data/us-cities
# import pandas
import requests
import json
from pathlib import Path


BEA_URL = "https://apps.bea.gov/api/data"
BEA_KEY = "8A864957-E515-4F60-9F2B-36245BDCC041"
BEA_PARAMS = {
    "UserID": BEA_KEY,
    "method": "GetData",
    "datasetname": "Regional",
    "TableName": None,
    "ResultFormat": "json",
}


def get_line_codes_for_table(table_name):
    params = {
        "UserID": BEA_KEY,
        "method": "GetParameterValuesFiltered",
        "datasetname": "Regional",
        "TableName": table_name,
        "TargetParameter": "LineCode",
        "ResultFormat": "json",
    }
    print(requests.get(BEA_URL, params=params).json())


def fetch_bea_data(table_name, line_code, datasheet):
    BEA_PARAMS["Year"] = "2020"
    BEA_PARAMS["GeoFIPS"] = "COUNTY"
    BEA_PARAMS["LineCode"] = line_code
    BEA_PARAMS["TableName"] = table_name

    bea_response = requests.get(BEA_URL, params=BEA_PARAMS)
    if bea_response.status_code == 200:
        json.dump(bea_response.json(), open(datasheet, "w"))
    else:
        print(bea_response.text)


PER_CAPITA_PERSONAL_INCOME = {
    "datasheet": "data/per_capita_personal_income.json",
    "table_name": "CAINC1",
    "line_code": 3,
}

TOTAL_EMPLOYMENT = {
    "datasheet": "data/total_employment.json",
    "table_name": "CAEMP25N",
    "line_code": 10,
}

AVERAGE_WAGES_AND_SALARIES = {
    "datasheet": "data/avg_wage_salaries.json",
    "table_name": "CAINC30",
    "line_code": 300,
}

PER_CAPITA_NET_EARNINGS = {
    "datasheet": "data/per_capita_net_earnings.json",
    "table_name": "CAINC30",
    "line_code": 120,
}

PER_CAPITA_DIVIDENDS_INTEREST_RENT = {
    "datasheet": "data/per_capita_dividends_interest_rent.json",
    "table_name": "CAINC30",
    "line_code": 170,
}

stats = [
    PER_CAPITA_PERSONAL_INCOME,
    TOTAL_EMPLOYMENT,
    AVERAGE_WAGES_AND_SALARIES,
    PER_CAPITA_NET_EARNINGS,
    PER_CAPITA_DIVIDENDS_INTEREST_RENT,
]

if __name__ == "__main__":

    for stat in stats:
        print(stat["datasheet"])
        if not Path(stat["datasheet"]).exists():
            fetch_bea_data(
                stat["table_name"],
                stat["line_code"],
                stat["datasheet"],
            )
