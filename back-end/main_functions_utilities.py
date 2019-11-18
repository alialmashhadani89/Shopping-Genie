import mail_credentations
import datetime
import web_scraping
from database_accessor import get_results, get_data_ai


# function to collect the date from best Buy website


def search_results_bestbuy(search_term):
    website_bb_info(search_term)

# function to collect the date from Walmart website


def search_results_walmart(search_term):
    website_wm_info(search_term)

# function to collect the date from Amazon website


def search_results_amazon(search_term):
    website_am_info(search_term)

# function to collect the date from B&H website


def search_results_bh(search_term):
    website_bh_info(search_term)


# check if the data out of date. if so then update for each store as needed.


def checkScrapingDate(search, results):

    todayDate = str(datetime.date.today())

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
    return results

# feeding the preidcation to the right place in the result table.


def storePredication(results, predication_price_list):
    for resultlist in results:
        if resultlist["storeName"] in predication_price_list:
            if float(predication_price_list[resultlist["storeName"]]) == 0:
                resultlist["predictionPrice"] = 'Not Enough Data'
                resultlist["predictionDate"] = 'No Date'
            else:
                resultlist["predictionPrice"] = str(
                    "$" + "{:.2f}".format(float(predication_price_list[resultlist["storeName"]])))

# scarping the 4 website for date


def webResult(search):
    search_results_bestbuy(search)
    search_results_bh(search)
    search_results_walmart(search)
    search_results_amazon(search)
    return get_results(search)

# getting the mail setting.


def mailCredentations():
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
    return mail_settings
