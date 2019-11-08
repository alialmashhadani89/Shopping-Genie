
from bs4 import BeautifulSoup
import requests
import re
from json_io import user_agent
from item_page_scraping_utilities import *


# Base URLs for the websites
bestbuy_base_url = "https://www.bestbuy.com/site/searchpage.jsp?st="
amazon_base_url = "https://www.amazon.com/s?k="
walmart_base_url = "https://www.walmart.com/search/?query="
bh_base_url = "https://www.bhphotovideo.com/c/search?sts=ma&N=0&pn=1&Ntt="

d_list = ["for"]
k_list_am = ["refurbished", "renewed"]
k_list_bh = ["refurbished"]
k_list_wm = ["refurbished"]
k_list_bb = ["refurbished", "pre-owned"]

def decrementScore(term_list, item_name):
    anti_score = 0

    for word in term_list:
        if word in item_name:
            anti_score += 1

    print("Anti-score: " + str(anti_score))
    return anti_score


def killScore(term_list, item_name):
    for word in term_list:
        if word in item_name:
            return True
            print("IT DEAD")

    return False

def check_item_uni(item_name, search_term, d_list, k_list):
    check_number = 0
    full_item_name = str(item_name).lower()
    for word in search_term.split():
        if len(word)>=2:
            score = full_item_name.count(word)
            if score == 1:
                check_number += 1

    check_number -= decrementScore(d_list, full_item_name)
    if killScore(k_list, full_item_name):
        check_number = 0

    print("Final Score: " + str(check_number))
    if check_number >= 2:
        return True
    else:
        return False
    # decrementList
    # deadlist 
    

# if the item not in the store, it will reject the search.
# in that case, we will save time and stop getting wrong items in out date bases.
def search_guard_bh(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append({"url": a["href"],
                      "name": a.find('span', {"itemprop": "name"}).get_text(),
                      "brand": a.find('span', {"itemprop": "brand"}).get_text()})
    #if check_item(links[0]["brand"], links[0]["name"], search_term):
    if check_item_uni(links[0]["name"], search_term, d_list, k_list_bh):
        return True
    else:
        return False

def search_guard_bb(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    name_headers = soup.find_all('h4', {"class": "sku-header"})
    item_name = []
    for header in name_headers:
        item_name.append(header.a.get_text())
    #if check_item_bb(item_name[0], search_term):
    if check_item_uni(item_name[0], search_term, d_list, k_list_bb):
        return True
    else:
        return False

def search_guard_wm(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "product-title-link line-clamp line-clamp-2"})
    print(len(anchors))
    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())
    #if check_item_wm(item_name[0], search_term):
    if check_item_uni(item_name[0], search_term, d_list, k_list_wm):
        return True
    else:
        return False

def search_guard_am(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "a-link-normal a-text-normal"})
    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())
    #if check_item_am(item_name[0], search_term):
    i = 0
    while i < 3:
        if check_item_uni(item_name[i], search_term, d_list, k_list_am):
            return True
        i+=1
    return False

# ====B&H====
# getting the info from the website.
def website_bh_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append({"url": a["href"],
                      "name": a.find('span', {"itemprop": "name"}).get_text(),
                      "brand": a.find('span', {"itemprop": "brand"}).get_text()})


    i = 0
    for link in links:
        #if check_item(link["brand"], link["name"], search_term):
        if check_item_uni(link["name"], search_term, d_list, k_list_bh):
            if i > 15:
                break
            outcome = page_parser_bandh(link["url"])
            if outcome:
                i+=1
            else:
                print("Not Available")
        else:
            print("Not relevant")

# get the response and convert it into lxml format.
def website_bh_info(search_term):
    link = bh_base_url + search_term

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_bh(response, search_term):

        website_bh_info_helping(response,search_term)

    else:
        print("We are sorry! The item you looking for is not in the B&H store")


#====Best Buy====
# getting the info from the website.
def website_bb_info_helping(response, search_term):
    # Cannot use check item because for bestbuy, brand name is not accessable at this stage
    soup = BeautifulSoup(response, 'lxml')
    headers = soup.find_all('h4', {"class": "sku-header"})
    links = []
    for header in headers:
        links.append({"url": "https://www.bestbuy.com" + header.a["href"],
                     "name": header.a.get_text() })

    i = 0
    for link in links:
        #if check_item_bb(link["name"], search_term):
        if check_item_uni(link["name"], search_term, d_list, k_list_bb):
            if i > 15:
                break
            outcome = page_parser_bestbuy(link["url"])
            if outcome:
                i += 1
            else:
                print("Not available")
        else:
            print("Not relevant")

# get the response and convert it into lxml format.
def website_bb_info(search_term):
    link = bestbuy_base_url + search_term

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_bb(response,search_term):

        website_bb_info_helping(response, search_term)

    else:
        print("We are sorry! The item you looking for is not in the Best Buy store")

#===Walmart===
# getting the info from the website.
def website_wm_info_helping(response, search_term):

    # Cannot use check item because for bestbuy, brand name is not accessable at this stage
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "product-title-link line-clamp line-clamp-2"})
    links = []
    for anchor in anchors:
        links.append({"url": "https://www.walmart.com" + anchor["href"],
                     "name": anchor.span.get_text()})

    i = 0
    for link in links:
        #if check_item_wm(link["name"], search_term):
        if check_item_uni(link["name"], search_term, d_list, k_list_wm):
            if i > 15:
                break
            outcome = page_parser_walmart(link["url"])
            if outcome:
                i+=1
            else:
                print("Not valid")
        else:
            print("Not relevant")

# get the response and convert it into lxml format.
def website_wm_info(search_term):
    link = walmart_base_url + search_term

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')
    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_wm(response,search_term):

        website_wm_info_helping(response, search_term)
    else:
        print("We are sorry! The item you looking for is not in the Walmart store")

#====Amazon====
# getting the info from the website.
def website_am_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')

    headers = soup.find_all('h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"})

    links = []

    for header in headers:
        if header.find_previous_sibling('a') == None:
            links.append( { "url": "https://www.amazon.com" + header.a["href"],
                            "name": header.a.span.get_text()})
    i = 0
    for link in links:
        #if check_item_am(link["name"], search_term):
        if check_item_uni(link["name"], search_term, d_list, k_list_am):
            if i > 15:
                break
            outcome = page_parser_amazon(link["url"])
            if outcome:
                i+=1
            else:
                print("Not valid")

        else:
            print("Not relevant")


# get the response and convert it into lxml format.
def website_am_info(search_term):
    link = amazon_base_url + search_term
    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_am(response,search_term):

        website_am_info_helping(response, search_term)
    else:
        print("We are sorry! The item you looking for is not in the Amazon store")
