
from bs4 import BeautifulSoup
import requests
import re
from json_io import *
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


# getting the info from the website.
def website_bh_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    anchors = soup.find_all('a', {"data-selenium": "itemHeadingLink"})
    links = []
    for a in anchors:
        links.append(a["href"])

    item_brand = soup.find_all('span', itemprop="brand")
    item_name = soup.find_all('span', itemprop="name")
    for link in links:
        if check_item(item_brand, item_name, search_term):
            page_parser_bandh(link)
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

        # If only one page
        if soup.find('div', class_="pagination-zone") == None:
           website_bh_info_helping(response,search_term)
        else:
            page_number_list = soup.find('div', class_="bottom pagination js-pagination clearfix left")
            page_number = page_number_list.find_all("a", class_="pn-btn active litGrayBtn")


            # getting the links
            for link in page_number:
                if link.has_attr('href'):
                    link_list.append(link['href'])
            page_number = page_number_list.find_all("a", class_="pn-btn litGrayBtn")
            for link in page_number:
                if link.has_attr('href'):
                    link_list.append(link['href'])

            # getting in info
            for links in link_list:
                response = requests.get(links, headers=user_agent, allow_redirects=True).text
                website_bh_info_helping(response,search_term)

    else:
        print("We are sorry! The item you looking for is not in the B&H store")

# getting the info from the website.
def website_bb_info_helping(response, search_term):
    # Cannot use check item because for bestbuy, brand name is not accessable at this stage
    soup = BeautifulSoup(response, 'lxml')
    headers = soup.find_all('h4', {"class": "sku-header"})
    links = []
    for header in headers:
        links.append("https://www.bestbuy.com" + header.a["href"])

    for link in links:
            page_parser_bestbuy(link)


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

        # If only one page
        if soup.find('ol', class_="paging-list") == None:
           website_bb_info_helping(response, search_term)
        else:
            page_number_list = soup.find('ol', class_="paging-list")
            page_number = page_number_list.find_all("a", class_="trans-button page-number")

            # getting the links
            for link in page_number:
                if link.has_attr('href'):
                    link_list.append(link['href'])

            # getting in info
            for links in link_list:
                response = requests.get(links, headers=user_agent, allow_redirects=True).text
                website_bb_info_helping(response, search_term)
                #page_parser_bestbuy(links)
    else:
        print("We are sorry! The item you looking for is not in the Best Buy store")
