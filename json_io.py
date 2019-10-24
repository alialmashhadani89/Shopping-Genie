# !flask/bin/python
import sys
import requests
from flask import Flask, render_template, request, redirect, Response, abort
import random, json
import time
from flask_assets import Bundle, Environment
from jinja2 import TemplateNotFound
from urllib.request import urlopen
import webbrowser
from googleapiclient.discovery import build
from web_scraping import *
from database_accessor import insertOneIntoQueryTable

# base url for the 3 website we using for the project.
bestbuy_base_url = "https://www.bestbuy.com/site/searchpage.jsp?st="
amazon_base_url = "https://www.amazon.com/s?k="
walmart_base_url = "https://www.walmart.com/search/?query="
bh_base_url = "https://www.bhphotovideo.com/c/search?sts=ma&N=0&pn=1&Ntt="
# to be accessed from the other file.
result_list = []

# to paypass the website restriction
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

app = Flask(__name__)

css = Bundle('style.css', output='styles/main.css')

assets = Environment(app)

assets.register('main_css', css)


def search_results_bestbuy(search_term):
    #response = requests.get(bestbuy_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    response = requests.get(bestbuy_base_url+search_term,headers=user_agent,allow_redirects=True).text
    #wesite_response_link(response)
    website_bb_info(bestbuy_base_url+search_term, search_term)

def search_results_walmart(search_term):
    #response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    #response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True).text
    #wesite_response_link(response)
    page_parser_walmart(walmart_base_url+search_term)

def search_results_amazon(search_term):
    #response = requests.get(amazon_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    response = requests.get(amazon_base_url + search_term, headers=user_agent, allow_redirects=True).text
    #wesite_response_link(response)

def search_results_bh(search_term):
    response = requests.get(bh_base_url + search_term, headers=user_agent, allow_redirects=True)
    # print(response.text)
    #response = requests.get(bh_base_url + search_term, headers=user_agent, allow_redirects=True).text
    #wesite_bh_info(bh_base_url+search_term)
    #website_bh_info(bh_base_url+search_term , search_term)



# the main API
@app.route('/api')
def api():
    search = request.args.get('search')

    # to search straight in in each website.
    search_results_bestbuy(search)
    #search_results_walmart(search)
    #search_results_amazon(search)
    #search_results_bh(search)

    return json.dumps({"search": search})

@app.route('/')
def output():
    return render_template('index.html')


@app.route('/about')
def aboutpage():
    return render_template('about.html')


@app.route('/index')
def indexpage():
    return render_template('index.html')


@app.route('/contact')
def contactpage():
    return render_template('contact.html')

@app.route('/feedback')
def feedbackpage():
    return render_template('feedback.html')



if __name__ == '__main__':
    # run!
    app.run(debug=True)


"""""
#The tags that comes with the search output. 

kind 
title ----------- (good)
htmlTitle 
link ------------ (good)
displayLink ----- (good)
snippet 
htmlSnippet 
cacheId
formattedUrl
htmlFormattedUrl
pagemap

"""""