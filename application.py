from flask import Flask
from flask import jsonify
from datetime import date
import urllib.request
import json

app = Flask(__name__)

@app.route("/getExchangeRate/<fromCurrency>/<toCurrency>")
def profile(fromCurrency, toCurrency):


    print("From currency: " + fromCurrency)
    print("To currency: " + toCurrency)

    url = "http://api.nbp.pl/api/exchangerates/tables/a/"
    json_obj = urllib.request.urlopen(url)

    data = json.load(json_obj)
    headers = {'Content-Type': 'application/json'}

    return jsonify(data)


if __name__ == "__main__":
    app.run()
