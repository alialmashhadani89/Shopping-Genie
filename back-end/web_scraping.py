
from bs4 import BeautifulSoup
import requests
import re
#from torrequest import TorRequest
from concealer import *
from item_page_scraping_utilities import *


# Base URLs for the websites
bestbuy_base_url = "https://www.bestbuy.com/site/searchpage.jsp?st="
amazon_base_url = "https://www.amazon.com/s?k="
walmart_base_url = "https://www.walmart.com/search/?query="
bh_base_url = "https://www.bhphotovideo.com/c/search?sts=ma&N=0&pn=1&Ntt="
bh_base_url2 = "https://www.bhphotovideo.com/c/search?Ntt=" 
# to paypass the website restriction

headers = {}
referer = "https://google.com"
# Words for which to decrement the link score
d_list = [" for ", " adapter ", " charger ", " case ", " cable ", " cover ", " screen "]
# Words for which to kill the link score
k_list_am = ["refurbished", "renewed"]
k_list_bh = ["refurbished"]
k_list_wm = ["refurbished"]
k_list_bb = ["refurbished", "pre-owned"]


# @pre  A link is being pre-evaluated
# @post  The number by which to detract from a link's score will be given
# @param  term_list  A list of words that would incur a one point penalty to a link's score
# @param  item_name  The item_name of the link in question
# @return  A number to be subtracted from the given link's score
def decrementScore(term_list, item_name):
    anti_score = 0
    for word in term_list:
        if word in item_name:
            #print(word)
            anti_score += 1

    #print("Anti-score: " + str(anti_score))
    return anti_score

# @pre  A link is being pre-evaluated
# @post  A judgement shall be rendered
# @param  term_list  A list of words for which to declare a link invalid
# @param  item_name  The item name of the link in question
# @return  True if invalid, False if Okay


def killScore(term_list, item_name):
    for word in term_list:
        if word in item_name:
            return True

    return False

# @pre  A link is being pre-evaluated
# @post  A judgement on whether or not to parse the link will be made
# @param  item_name  The item name of the link in question
# @param  search_term  The words searched for the given query
# @param  d_list  A list of words with which to decrement a link's score
# @param  k_list  A list of words for which to tank a link's score
# @return  True if link is valid, otherwise False


def check_item_uni(item_name, search_term, d_list, k_list, store):
    score = 0
    term_count = len(search_term.split())
    full_item_name = str(item_name).lower()

    occurence_count = 0
    for word in search_term.split():
        fluff = " " + word + " "
        if len(word)>=2:
            if str(fluff).lower() in full_item_name:

                occurence_count += 1


    if term_count == occurence_count:
        score = 2
    else:
        return False

    score -= decrementScore(d_list, full_item_name)
    if killScore(k_list, full_item_name):
        score = 0

    if score >= 2:
        return True
    else:
        return False


# if the item not in the store, it will reject the search.
# in that case, we will save time and stop getting wrong items in out date bases.
# @pre  A search page is being parsed
# @post A judgement regarding the validity of the result will be made
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
# @return  True if the page is valid, otherwise false.
def search_guard_bh(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append({"url": a["href"],
                      "name": a.find('span', {"itemprop": "name"}).get_text()})

    if len(links) == 0:
        return False

    if check_item_uni(links[0]["name"], search_term, d_list, k_list_bh, "B&H"):
        return True
    else:
        return False

# @pre  A search page is being parsed
# @post A judgement regarding the validity of the result will be made
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
# @return  True if the page is valid, otherwise false.


def search_guard_bb(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    name_headers = soup.find_all('h4', {"class": "sku-header"})
    item_name = []
    for header in name_headers:
        item_name.append(header.a.get_text())

    if len(item_name) == 0:
        print("Page empty of links")
        return False

    if check_item_uni(item_name[0], search_term, d_list, k_list_bb, "Best Buy"):
        return True
    else:
        return False

# @pre  A search page is being parsed
# @post A judgement regarding the validity of the result will be made
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
# @return  True if the page is valid, otherwise false.


def search_guard_wm(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all(
        'a', {"class": "product-title-link line-clamp line-clamp-2"})
    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())

    if len(item_name) == 0:
        return False

    if check_item_uni(item_name[0], search_term, d_list, k_list_wm, "Walmart"):
        return True
    else:
        return False

# @pre  A search page is being parsed
# @post A judgement regarding the validity of the result will be made
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
# @return  True if the page is valid, otherwise false.


def search_guard_am(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "a-link-normal a-text-normal"})

    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())


    if len(item_name) == 0:
        print("Page empty of links")
        return False

    i = 0
    for name in item_name:
        if i < 3:
            #print("Run #: " + str(i))
            if check_item_uni(name, search_term, d_list, k_list_am, "Amazon"):
                return True
            i += 1
        else:
            return False


def info_requester(link, package, search_term):
    try:
        #tr = TorRequest(password="hashpass")
        #tr.reset_identity()
        headers = package["user_agent"]

        # Opening the pages and check how many page numbers
        #result = package["tr"].get(link, headers=headers)
        result = requests.get(link, headers=headers,
                            allow_redirects=True)
        response = result.text
        print(result.url)
        soup = BeautifulSoup(response, 'lxml')

        return response
    except:
        #print("Problem")
        package["count"] = 3
        package = getPackage(package)
        # Try again with new package
        return info_requester(link, package, search_term)



# ====B&H====
# getting the info from the website.
# @pre  A search page has been cleared for parsing
# @post  Item pages will possibly be parsed.
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching

def website_bh_info_helping(response, search_term, package):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append({"url": a["href"],
                      "name": a.find('span', {"itemprop": "name"}).get_text()})

    i = 0
    for link in links:
        if check_item_uni(link["name"], search_term, d_list, k_list_bh, "B&H"):
            if i > 15:
                break

            package = getPackage(package)
            outcome = page_parser_bandh(link["url"], package)
            if outcome:
                i += 1
            else:
                z = 0
                #print("Not Available")
        else:
            z = 0
            #print("Not relevant")

# @pre  A web search has begun
# @post  Results will possibly be gathered.
# @param  search_term  The given search term made by the user.


def website_bh_info(search_term):
    link = bh_base_url2 + search_term.replace(" ", "%20")
    print(link)

    package = getPackage(None)
    response = info_requester(link, package, search_term)


    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_bh(response, search_term):

        website_bh_info_helping(response, search_term, package)

    else:
        print("We are sorry! The item you looking for is not in the B&H store")


# ====Best Buy====
# getting the info from the website.
# @pre  A search page has been cleared for parsing
# @post  Item pages will possibly be parsed.
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
def website_bb_info_helping(response, search_term, package):
    soup = BeautifulSoup(response, 'lxml')
    headers = soup.find_all('h4', {"class": "sku-header"})
    links = []
    for header in headers:
        links.append({"url": "https://www.bestbuy.com" + header.a["href"],
                      "name": header.a.get_text()})

    i = 0
    for link in links:
        if check_item_uni(link["name"], search_term, d_list, k_list_bb, "Best Buy"):
            if i > 15:
                break

            package = getPackage(package)
            outcome = page_parser_bestbuy(link["url"], package)
            if outcome:
                i += 1
            else:
                z = 0
                #print("Not available")
        else:
            z = 0
            #print("Not relevant")

# get the response and convert it into lxml format.
# @pre  A web search has begun
# @post  Results will possibly be gathered.
# @param  search_term  The given search term made by the user.


def website_bb_info(search_term):
    link = bestbuy_base_url + search_term

    package = getPackage(None)
    response = info_requester(link, package, search_term)
    #soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_bb(response, search_term):

        website_bb_info_helping(response, search_term, package)

    else:
        print("We are sorry! The item you looking for is not in the Best Buy store")

# ===Walmart===
# @pre  A search page has been cleared for parsing
# @post  Item pages will possibly be parsed.
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
# getting the info from the website.
def website_wm_info_helping(response, search_term, package):

    # Cannot use check item because for bestbuy, brand name is not accessable at this stage
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all(
        'a', {"class": "product-title-link line-clamp line-clamp-2"})
    links = []
    for anchor in anchors:
        links.append({"url": "https://www.walmart.com" + anchor["href"],
                      "name": anchor.span.get_text()})

    i = 0
    for link in links:
        if check_item_uni(link["name"], search_term, d_list, k_list_wm, "Walmart"):
            if i > 15:
                break
            package = getPackage(package)
            outcome = page_parser_walmart(link["url"], package)
            if outcome:
                i += 1
            else:
                z = 0
                #print("Not valid")
        else:
            z = 0
            #print("Not relevant")

# get the response and convert it into lxml format.
# @pre  A web search has begun
# @post  Results will possibly be gathered.
# @param  search_term  The given search term made by the user.
def website_wm_info(search_term):
    link = walmart_base_url + search_term.replace(" ", "%20")
    package = getPackage(None)
    response = info_requester(link, package, search_term)

    #soup = BeautifulSoup(response, 'lxml')
    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_wm(response, search_term):

        website_wm_info_helping(response, search_term, package)
    else:
        print("We are sorry! The item you looking for is not in the Walmart store")

# ====Amazon====
# getting the info from the website.
# @pre  A search page has been cleared for parsing
# @post  Item pages will possibly be parsed.
# @param  response  The HTML response of the page in question
# @param  search_term  The term a given user is searching
def website_am_info_helping(response, search_term, package):
    soup = BeautifulSoup(response, 'lxml')

    htwos = soup.find_all(
        'h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"})

    links = []

    for header in htwos:
        if header.find_previous_sibling('a') == None:
            links.append({"url": "https://www.amazon.com" + header.a["href"],
                          "name": header.a.span.get_text()})
    i = 0
    for link in links:
        if check_item_uni(link["name"], search_term, d_list, k_list_am, "Amazon"):
            if i > 15:
                break
            package = getPackage(package)
            outcome = page_parser_amazon(link["url"], package)
            if outcome:
                i += 1
            else:
                z = 0
                #print("Not valid")

        else:
            z = 0
            #print("Not relevant")


# get the response and convert it into lxml format.
# @pre  A web search has begun
# @post  Results will possibly be gathered.
# @param  search_term  The given search term made by the user.
def website_am_info(search_term):
    
    link = amazon_base_url + search_term.replace(" ", "+")

    package = getPackage(None)
    response = info_requester(link, package, search_term)
    #soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_am(response, search_term):

        website_am_info_helping(response, search_term, package)
    else:
        print("We are sorry! The item you looking for is not in the Amazon store")
