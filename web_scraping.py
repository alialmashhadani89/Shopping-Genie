
from bs4 import BeautifulSoup
import requests
import re
from json_io import user_agent
from item_page_scraping_utilities import *

def check_item(item_brand, item_name, search_term):
    check_number = 0
    full_item_name = str(item_brand[0].text).lower() + " " + str(item_name[0].text).lower()
    for word in search_term.split():
        if len(word)>=2:
            if str(word).lower() in full_item_name:
                check_number += 1
    if check_number >= 2:
        return True
    else:
        return False

def check_item_bb(item_name, search_term):
    print(item_name)
    check_number = 0
    full_item_name = str(item_name[0]).lower()
    for word in search_term.split():
        if len(word)>=2:
            if str(word).lower() in full_item_name:
                check_number += 1
    if check_number >= 2:
        return True
    else:
        return False

def check_item_wm(item_name, search_term):
    check_number = 0
    full_item_name = str(item_name[0]).lower()
    for word in search_term.split():
        if len(word)>=2:
            if str(word).lower() in full_item_name:
                check_number += 1
    if check_number >= 2:
        return True
    else:
        return False

def check_item_am(item_name, search_term):
    check_number = 0
    full_item_name = str(item_name).lower()
    #print(full_item_name)

    for word in search_term.split():
        #print(word)

        if len(word)>=2:
            #   if str(word).lower() in full_item_name:
            #        check_number += 1
            score = full_item_name.count(word)
            #print(score)
            if score == 1:
                check_number += 1

    if "for" in full_item_name:
        check_number -= 1
    if check_number >= 2:
        return True
    else:
        return False

# if the item not in the store, it will reject the search.
# in that case, we will save time and stop getting wrong items in out date bases.
def search_guard_bh(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    item_name = soup.find_all('span', itemprop="name")
    item_brand = soup.find_all('span', itemprop="brand")
    if check_item(item_brand, item_name, search_term):
        return True
    else:
        return False

def search_guard_bb(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    name_headers = soup.find_all('h4', {"class": "sku-header"})
    item_name = []
    for header in name_headers:
        item_name.append(header.a.get_text())
    if check_item_bb(item_name, search_term):
        return True
    else:
        return False

def search_guard_wm(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "product-title-link line-clamp line-clamp-2"})
    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())
    if check_item_wm(item_name, search_term):
        return True
    else:
        return False

def search_guard_am(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "a-link-normal a-text-normal"})
    item_name = []
    for anchor in anchors:
        item_name.append(anchor.span.get_text())
    if check_item_am(item_name[0], search_term):
        return True
    else:
        return False

# ====B&H====
# getting the info from the website.
def website_bh_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append(a["href"])

    item_brand = soup.find_all('span', itemprop="brand")
    item_name = soup.find_all('span', itemprop="name")

    i = 0
    for link in links:
        if check_item(item_brand, item_name, search_term):
            if i > 15:
                break
            page_parser_bandh(link)
            i+=1
        else:
            print("Not relevant")

# get the response and convert it into lxml format.
def website_bh_info(link,search_term):
    # list that will store all the links needed
    link_list = []

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
        links.append("https://www.bestbuy.com" + header.a["href"])

    i = 0
    for link in links:
        if i > 15:
            break
        outcome = page_parser_bestbuy(link)
        if outcome:
            i += 1

# get the response and convert it into lxml format.
def website_bb_info(link, search_term):
    # list that will store all the links needed
    link_list = []

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
    print("Walmart Helping Info")
    # Cannot use check item because for bestbuy, brand name is not accessable at this stage
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"class": "product-title-link line-clamp line-clamp-2"})
    links = []
    print(len(anchors))
    for anchor in anchors:
        links.append("https://www.walmart.com" + anchor["href"])

    i = 0
    for link in links:
        if i > 15:
            break
        page_parser_walmart(link)
        i+=1

# get the response and convert it into lxml format.
def website_wm_info(link, search_term):
    # list that will store all the links needed
    print(link)
    link_list = []

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')
    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_wm(response,search_term):

        # If only one page

#        button = None
#        if button == None:
#            print("One Page")
        website_wm_info_helping(response, search_term)
#        else:
#            print("Many Page")
#            page_number_list = soup.find('ul', class_="paginator-list")
#            page_number = page_number_list.find_all('a')

            # getting the links
#            for link in page_number:
#                if link.has_attr('href'):
#                    link_list.append(link['href'])

            # getting in info
#            for links in link_list:
#                response = requests.get(links, headers=user_agent, allow_redirects=True).text
#                website_wm_info_helping(response, search_term)
    else:
        print("We are sorry! The item you looking for is not in the Walmart store")

#====Amazon====
# getting the info from the website.
def website_am_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')

    # The specific sibling to avoid is "a-row a-spacing-micro"
    headers = soup.find_all('h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    item_name = soup.find_all('span', {"class": "a-size-medium a-color-base a-text-normal"})

    links = []

    # MUST FILTER OUt SPONSERED CONTENT. CHECK SIBLING. IF HAS "micro spacing" nonsense, dont accept
    for header in headers:
        if header.find_previous_sibling('a') == None: #and header.find_previous_sibling('a')["class"]!= "a-row a-spacing-micro":
            links.append( { "link": "https://www.amazon.com" + header.a["href"],
                            "name": header.a.span.get_text()})
    i = 0
    for link in links:
        if check_item_am(link["name"], search_term):
            if i > 15:
                break
            outcome = page_parser_amazon(link["link"])
            if outcome:
                #print("Link#: " + str(i))
                i+=1
            else:
                print("OUT OF STOCK OR OTHER")

        else:
            print("NOT VALID")

        #print("======")
# get the response and convert it into lxml format.
def website_am_info(link, search_term):

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard_am(response,search_term):

        website_am_info_helping(response, search_term)
    else:
        print("We are sorry! The item you looking for is not in the Amazon store")
