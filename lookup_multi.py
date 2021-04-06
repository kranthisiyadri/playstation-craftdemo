import sys
from lookup import getall_countrycodes_api
from lookup_file import getall_countrycodes_fromfile
from pprint import pprint


if __name__ == '__main__':
    country_code_string = sys.argv[1]
    country_code_arr = country_code_string.split("=")[1]
    country_codes = country_code_arr.split(",")
    all_country_info = getall_countrycodes_fromfile()
    for country_code in country_codes:
        country_name = all_country_info[country_code]
        pprint ("{}".format(country_name))
