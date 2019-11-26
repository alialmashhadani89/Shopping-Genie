import sys
import requests
from flask import Flask, render_template, request, redirect, Response, abort
import json
from flask_assets import Bundle, Environment
from database_accessor import get_results, get_data_ai
from flask_cors import CORS
from flask_mail import Mail, Message
from main_functions_utilities import *


app = Flask(__name__)
CORS(app)


# the main API
@app.route('/api')
def api():
    search = request.args.get('search')
    # to search straight in in each website.
    webResult(search)
    return json.dumps({"search": search})


@app.route('/api/results')
def results():
    search = request.args.get('search')
    results = get_results(search)

    # if we don't have the item in the databases, we will do webScripong.
    
    if len(results) == 0:
        results = webResult(search)
    else:
        # if we have then we check store by store if it out of date.
        results = checkScrapingDate(search, results)

    # getting the preidcation per store
    predication_price_list = get_data_ai(search)
    # print(predication_price_list)

    # giving the predication to each raw in the data.
    # Note: if the data is not enpugh, we will tell the user.
    storePredication(results, predication_price_list)

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
    #creds = getCredentials()
    mail_settings = mailCredentations()

    # composed the date we colleced from the website to the mail.
    # second the data in an email to us.
    app.config.update(mail_settings)
    mail = Mail(app)
    with app.app_context():
        msg = Message(subject="Feedback",
                      recipients=[mail_settings["MAIL_USERNAME"]],
                      # this is where we will put the content of the email.
                      body=data['name'] + ", \n\n" + data['email'] + "; \n\n" + data['content'])
        mail.send(msg)
        # we can put alert that mail has been sent.
        return json.dumps({"message": "Message sent successfully"})


if __name__ == '__main__':
    # run!
    app.run(debug=True)
