# !flask/bin/python
import sys
import requests
from flask import Flask, render_template, request, redirect, Response, abort
import random
import json
import time
from flask_assets import Bundle, Environment
from jinja2 import TemplateNotFound
from urllib.request import urlopen
from web_scraping import *
from database_accessor import get_results, get_data_ai
from flask_cors import CORS
from flask_mail import Mail, Message
from mail_credentations import getCredentials



app = Flask(__name__)
CORS(app)


def search_results_bestbuy(search_term):
    website_bb_info(search_term)


def search_results_walmart(search_term):
    website_wm_info(search_term)


def search_results_amazon(search_term):
    website_am_info(search_term)


def search_results_bh(search_term):
    website_bh_info(search_term)


# the main API
@app.route('/api')
def api():
    search = request.args.get('search')

    # to search straight in in each website.
    search_results_bestbuy(search)
    search_results_walmart(search)
    search_results_amazon(search)
    search_results_bh(search)

    return json.dumps({"search": search})


@app.route('/api/results')
def results():
    search = request.args.get('search')
    results = get_results(search)
    if (len(results) == 0):
        search_results_bestbuy(search)
        search_results_bh(search)
        search_results_walmart(search)
        search_results_amazon(search)
        results = get_results(search)

    predication_price = float(' '.join(map(str, get_data_ai(search))))
    for resultlist in results:
        resultlist["predictionPrice"] = str(
            "$" + "{:.2f}".format(predication_price))
    # giving the seatch term to get the prices of the product.
    """
    predictions = [{"brand": "B&H", "prediction": "0"},
                   {"brand": "Best Buy", "prediction": "$0"},
                   {"brand": "Amazon", "prediction": "0"},
                   {"brand": "Walmart", "prediction": "0"}]

    for i in range(len(results)):
        result = results[i]
        for x in predictions:
            if x["brand"] == result["storeName"]:
                result.update(
                    {"prediction": str("$" + ' '.join(map(str, predication_price)))})
        results[i] = result
    """
    return json.dumps(results)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/api/feedbackmail', methods=["POST"])
def sendmail():
    data = request.get_json(force=True)
    creds = getCredentials()
    mail_settings = {
        "MAIL_SERVER": creds["MAIL_SERVER"],
        "MAIL_PORT": creds["MAIL_PORT"],
        "MAIL_USE_TLS": creds["MAIL_USE_TLS"],
        "MAIL_USE_SSL": creds["MAIL_USE_SSL"],
        "MAIL_USERNAME": creds["MAIL_USERNAME"],
        "MAIL_PASSWORD": creds["MAIL_PASSWORD"],
        "MAIL_DEFAULT_SENDER": creds["MAIL_DEFAULT_SENDER"]
    }

    app.config.update(mail_settings)
    mail = Mail(app)
    with app.app_context():
        msg = Message(subject="Feedback",
                      recipients=["pricegenie0499@gmail.com"],
                      # this is where we will put the content of the email.
                      body=data['name'] + ", \n\n" + data['email'] + "; \n\n" + data['content'])
        mail.send(msg)
        # we can put alert that mail has been sent.
        return json.dumps({"message": "Message sent successfully"})


if __name__ == '__main__':
    # run!
    app.run(debug=True)
