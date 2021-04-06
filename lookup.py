import sys
import requests
from requests.exceptions import HTTPError

from pprint import pprint

def getall_countrycodes_api():
    """
    Get All Country Codes
    returns: ([dictionary]): dictionary of countries with country_code as key  country_name as value
    """
    all_countries_dict = dict()

    countrycode_api_url = "https://www.travel-advisory.info/api"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(
            countrycode_api_url, headers=headers, verify=False
        )
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        response_json = response.json()
        all_countries = response_json['data']
        # pprint(all_countries.keys())
        for country in all_countries.keys():
            country_info = all_countries[country]
            country_name = country_info['name']
            all_countries_dict[country] = country_name
        # pprint(all_countries)
        return all_countries_dict
    except HTTPError as http_err:
        print("HTTP error occurred: {}".format(http_err))
        return ""
    except Exception as err:
        print("Other error occurred: {}".format(err))
        return ""

def lookup(argv):
    country_code_string = argv[1]
    country_code_arr = country_code_string.split("=")
    country_code = country_code_arr[1]
    all_country_info = getall_countrycodes_api()
    # pprint(all_country_info)
    country_name = all_country_info[country_code]
    pprint (country_name)


if __name__ == '__main__':
    lookup(sys.argv)
