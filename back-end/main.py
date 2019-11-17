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
import datetime


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
    todayDate = str(datetime.date.today())
    results = get_results(search)
    tableDate = '2000-01-01'

    # if we don't have the item in the databases, we will do webScripong.
    if len(results) == 0:
        search_results_bestbuy(search)
        search_results_bh(search)
        search_results_walmart(search)
        search_results_amazon(search)
        results = get_results(search)
    else:
        # if we have then we check store by store if it out of date.
        for resultlist in results:
            if str(resultlist['storeName']) == 'Best Buy' and todayDate != resultlist['todayDateTable']:
                search_results_bestbuy(search)
            elif str(resultlist['storeName']) == 'B&H' and todayDate != resultlist['todayDateTable']:
                search_results_bh(search)
            elif str(resultlist['storeName']) == 'Amazon' and todayDate != resultlist['todayDateTable']:
                search_results_amazon(search)
            elif str(resultlist['storeName']) == 'Walmart' and todayDate != resultlist['todayDateTable']:
                search_results_walmart(search)
            results = get_results(search)

    # getting the preidcation per store
    predication_price_list = get_data_ai(search)
    # print(predication_price_list)

    # giving the predication to each raw in the data.
    # Note: if the data is not enpugh, we will tell the user.
    for resultlist in results:
        for i in predication_price_list:
            if i == resultlist["storeName"]:
                if predication_price_list[i] == '0':
                    resultlist["predictionPrice"] = 'Not Enough Data'
                    resultlist["predictionDate"] = 'No Date'
                else:
                    resultlist["predictionPrice"] = str(
                        "$" + "{:.2f}".format(float(predication_price_list[i])))

    # giving the seatch term to get the prices of the product.
    return json.dumps(results)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

# the feed back mail function and route
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

    # composed the date we colleced from the website to the mail.
    # second the data in an email to us.
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
