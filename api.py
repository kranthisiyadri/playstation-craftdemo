from flask import Flask,  jsonify
import sys
import json
# from flask.ext.cors import CORS, cross_origin
from flask_cors import CORS
from flask_cors import cross_origin
from flask import Response, request
import requests
from requests.exceptions import HTTPError


from lookup_file import getall_countrycodes_fromfile
from lookup import getall_countrycodes_api


app = Flask(__name__)
app.config["DEBUG"] = True
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route("/")
@cross_origin()
def home():
    return "<h1>Welcome</h1>"

@app.route('/health', methods=['GET'])
def check_health():
    return Response("Status OK", mimetype="application/json", status=200)

@app.route('/diag', methods=['GET'])
def get_diag():
    countrycode_api_url =    "https://www.travel-advisory.info/api"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(
            countrycode_api_url,  headers=headers, verify=False
        )
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        response_json = response.json()
        api_status = response_json['api_status']
    except HTTPError as http_err:
        print("HTTP error occurred: {}".format(http_err))
        return ""
    except Exception as err:
        print("Other error occurred: {}".format(err))
        return ""
    return Response(json.dumps({'api_status':api_status}, default=str), mimetype="application/json", status=200)

@app.route('/convert/<country_name>', methods=['GET'])
def get_countrycode(country_name):
    all_country_info = getall_countrycodes_fromfile()

    all_country_info = {v: k for k, v in all_country_info.items()}
    countrycode = all_country_info[country_name]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(countrycode)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
