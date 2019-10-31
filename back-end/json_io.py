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


# base url for the 3 website we using for the project.
bestbuy_base_url = "https://www.bestbuy.com/site/searchpage.jsp?st="
amazon_base_url = "https://www.amazon.com/s?k="
walmart_base_url = "https://www.walmart.com/search/?query="
bh_base_url = "https://www.bhphotovideo.com/c/search?sts=ma&N=0&pn=1&Ntt="
# to be accessed from the other file.
result_list = []

# to paypass the website restriction
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

app = Flask(__name__)
CORS(app)


css = Bundle('style.css', output='styles/main.css')

assets = Environment(app)

assets.register('main_css', css)


def search_results_bestbuy(search_term):
    #response = requests.get(bestbuy_base_url + search_term, headers=user_agent, allow_redirects=True)
    # print(response.text)
    response = requests.get(bestbuy_base_url+search_term,
                            headers=user_agent, allow_redirects=True).text
    # wesite_response_link(response)
    website_bb_info(bestbuy_base_url+search_term, search_term)


def search_results_walmart(search_term):
    #response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True)
    # print(response.text)
    #response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True).text
    # wesite_response_link(response)
    page_parser_walmart(walmart_base_url+search_term)


def search_results_amazon(search_term):
    #response = requests.get(amazon_base_url + search_term, headers=user_agent, allow_redirects=True)
    # print(response.text)
    response = requests.get(amazon_base_url + search_term,
                            headers=user_agent, allow_redirects=True).text
    # wesite_response_link(response)


def search_results_bh(search_term):
    return website_bh_info(bh_base_url+search_term, search_term)


# the main API
@app.route('/api/search')
def search():
    search = request.args.get('search')

    # to search straight in in each website.
    search_results_bestbuy(search)
    # search_results_walmart(search)
    # search_results_amazon(search)
    results = search_results_bh(search)

    return json.dumps({"results": results})


@app.route('/api/results')
def results():
    search = request.args.get('search')
    # giving the seatch term to get the prices of the product.
    predication_price = get_data_ai(search)
    print(predication_price)
    return json.dumps(get_results(search))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/feebbackmail')
def sendmail():
    mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": 'pricegenie0499@gmail.com',
        "MAIL_PASSWORD": 'shoppinggenie499',
        "MAIL_DEFAULT_SENDER": 'pricegenie0499@gmail.com'
    }

    app.config.update(mail_settings)
    mail = Mail(app)
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("pricegenie0499@gmail.com"),
                      # replace with your email for testing
                      recipients=["pricegenie0499@gmail.com"],
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)
        return "Message has been sent!"


if __name__ == '__main__':
    # run!
    app.run(debug=True)
