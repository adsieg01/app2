from flask import Flask, jsonify
import requests
import json
import dns

app = Flask(__name__)

@app.route("/")
def home():
    url = "http://atlas-infra-connect-2.cdf-infra.appserviceenvironment.net/"
    res = requests.get(url)
    dictFromServer = res.json()
    return dictFromServer['message']


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
   
