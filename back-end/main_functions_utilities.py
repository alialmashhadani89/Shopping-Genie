from mail_credentations import getCredentials
import datetime
import web_scraping
import database_accessor


# function to collect the date from best Buy website


def search_results_bestbuy(search_term):
    web_scraping.website_bb_info(search_term)

# function to collect the date from Walmart website


def search_results_walmart(search_term):
    web_scraping.website_wm_info(search_term)

# function to collect the date from Amazon website


def search_results_amazon(search_term):
    web_scraping.website_am_info(search_term)

# function to collect the date from B&H website


def search_results_bh(search_term):
    web_scraping.website_bh_info(search_term)


# check if the data out of date. if so then update for each store as needed.


def checkScrapingDate(search, results):
    todayDate = str(datetime.date.today())
    storeList =[]
    # getting the list of store we current have in the databases.
    for resultlist in results:
        storeList.append(str(resultlist['storeName']))
    
    # check if each store in the databases up to date.
    for resultlist in results:
        if str(resultlist['storeName']) == 'Best Buy' and todayDate != resultlist['todayDateTable']:
            search_results_bestbuy(search)
        elif str(resultlist['storeName']) == 'B&H' and todayDate != resultlist['todayDateTable']:
            search_results_bh(search)
        elif str(resultlist['storeName']) == 'Amazon' and todayDate != resultlist['todayDateTable']:
            search_results_amazon(search)
        elif str(resultlist['storeName']) == 'Walmart' and todayDate != resultlist['todayDateTable']:
            search_results_walmart(search)
    
    # if the store not even in the databses, then we need to do some webscriping for one more time. 
    if 'Best Buy' not in storeList:
        search_results_bestbuy(search)
    elif 'B&H' not in storeList:
        search_results_bh(search)
    elif 'Amazon' not in storeList:
        search_results_amazon(search)
    elif 'Walmart' not in storeList:
        search_results_walmart(search)
    
    # uodating the result list after all the update we did above.    
    results = database_accessor.get_results(search)
    
    # return the final result. 
    return results
    
# feeding the preidcation to the right place in the result table.


def storePredication(results, predication_price_list):
    for resultlist in results:
        if resultlist["storeName"] in predication_price_list:
            if float(predication_price_list[resultlist["storeName"]]) == 0:
                resultlist["predictionPrice"] = 'Not enough data!'
                resultlist["predictionDate"] = ' '
            else:
                resultlist["predictionPrice"] = str(
                    "$" + "{:.2f}".format(float(predication_price_list[resultlist["storeName"]])))


# scarping the 4 website for date


def webResult(search):
    search_results_bestbuy(search)
    search_results_bh(search)
    search_results_walmart(search)
    search_results_amazon(search)
    return database_accessor.get_results(search)

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
