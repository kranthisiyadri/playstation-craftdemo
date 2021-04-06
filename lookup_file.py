import sys
import json
from pprint import pprint

def getall_countrycodes_fromfile():
    all_countries_dict = dict()
    print ("Reading country codes from JSON file")
    # curl https://www.travel-advisory.info/api -o data.json

    with open('data.json') as country_fh:
        data = json.load(country_fh)
        all_countries = data['data']
        for country in all_countries.keys():
            country_info = all_countries[country]
            country_name = country_info['name']
            all_countries_dict[country] = country_name
    return all_countries_dict


def lookup_file(argv):
    country_code_string = argv[1]
    country_code_arr = country_code_string.split("=")
    country_code = country_code_arr[1]
    all_country_info = getall_countrycodes_fromfile()
    # pprint(all_country_info)
    country_name = all_country_info[country_code]
    pprint (country_name)


if __name__ == '__main__':
    lookup_file(sys.argv)
