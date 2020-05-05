from flask import Flask
from datetime import date
from flask_json_api import FlaskJsonApi
import urllib.request
import json

app = Flask(__name__)
flask_json_api = FlaskJsonApi(app)

@app.route("/<ExchangeRatesTable>/<fromCurrency>/<toCurrency>")
def profile(fromCurrency, toCurrency):
    pass


url = "http://api.nbp.pl/api/exchangerates/tables/a/"
json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)
headers = {'Content-Type': 'application/json'}

print(data)
