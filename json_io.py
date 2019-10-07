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

# base url for the 3 website we using for the project.
bestbuy_base_url = "https://www.bestbuy.com/site/searchpage.jsp?st="
amazon_base_url = "https://www.amazon.com/s?k="
walmart_base_url = "https://www.walmart.com/search/?query="
bh_base_url = "https://www.bhphotovideo.com/c/search?Ntt="
# to be accessed from the other file.
result_list = []

# to paypass the website restriction
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

# my API key for the google search engine.
api_key = "AIzaSyCJjHkpKCmznN_gvY9KJK1I-YQWiqdvKrA"

# we build the search engine.
resource = build(serviceName ="customsearch", version = "v1", developerKey=api_key).cse()

app = Flask(__name__)

css = Bundle('style.css', output='styles/main.css')

assets = Environment(app)

assets.register('main_css', css)

# to print with time out.
def print_result(item):
    time.sleep(2)
    print(item['title'], item['link'])


def search_result_with_google(input):
    finalResult = []

    # from what number to what
    for i in range(1, 20, 10):
        result = resource.list(q=input, cx='007105990500405929801:dz5kgdlvpxl', start=i).execute()
        finalResult += result['items']

    for item in finalResult:
        print_result(item)
    result_list = finalResult


def search_results_bestbuy(search_term):
    #response = requests.get(bestbuy_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    response = requests.get(bestbuy_base_url+search_term,headers=user_agent,allow_redirects=True).text
    wesite_response_link(response)

def search_results_walmart(search_term):
    #response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    response = requests.get(walmart_base_url + search_term, headers=user_agent, allow_redirects=True).text
    wesite_response_link(response)

def search_results_amazon(search_term):
    #response = requests.get(amazon_base_url + search_term, headers=user_agent, allow_redirects=True)
    #print(response.text)
    response = requests.get(amazon_base_url + search_term, headers=user_agent, allow_redirects=True).text
    wesite_response_link(response)

def search_results_bh(search_term):
    #response = requests.get(bh_base_url + search_term, headers=user_agent, allow_redirects=True)
    # print(response.text)
    response = requests.get(bh_base_url + search_term, headers=user_agent, allow_redirects=True).text
    wesite_response_link(response)


# the main API
@app.route('/api')
def api():
    search = request.args.get('search')

    # to use google search engine
    search_result_with_google(search) # bing question mark.

    # to search straight in in each website.
    #search_results_bestbuy(search)
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


Note for the next class:

* to avoid using a confusing (one word) words that might start pulling products we don't need. 
* web scarping?
* store the info we need in the databases (MySql)
* finish the details page so we can put the info from (databases) on it or from the search result.
* working on the other pages. 
* for the feedback page, we need to store the input in something so we can review it.
* we might need to change amazon for B&H website since it bing bad


"""""