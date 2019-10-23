
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


# if the item not in the store, it will reject the search.
# in that case, we will save time and stop getting wrong items in out date bases.
def search_guard(response,search_term):
    soup = BeautifulSoup(response, 'lxml')
    item_name = soup.find_all('span', itemprop="name")
    item_brand = soup.find_all('span', itemprop="brand")
    if check_item(item_brand,item_name,search_term):
        return True
    else:
        return False


# getting the info from the website.
def website_bh_info_helping(response, search_term):
    soup = BeautifulSoup(response, 'lxml')
    links = soup.find_all('a', {"data-selenium": "itemHeading"})
    #price = soup.find_all('span', class_="itc-you-pay-price bold")
    item_brand = soup.find_all('span', itemprop="brand")
    item_name = soup.find_all('span', itemprop="name")
    #images = soup.find_all('img', {'src':re.compile('.jpg')})
    #for i in range(len(price)):
    #    if check_item(item_brand, item_name, search_term):
    #        print(item_brand[i].text + " " + item_name[i].text + " " + price[i].text + " " + images[i] ['src'])
    for link in links:
        if check_item(item_brand, item_name, search_term):
            page_parser_bandh(link)




# get the response and convert it into lxml format.
def website_bh_info(link,search_term):
    # list that will store all the links needed
    link_list = []

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard(response,search_term):

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

# get the response and convert it into lxml format.
def website_bb_info(link, search_term):
    # list that will store all the links needed
    link_list = []

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard(response,search_term):

        # If only one page
        if soup.find('ol', class_="paging-list") == None:
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
               # response = requests.get(links, headers=user_agent, allow_redirects=True).text
               # website_bh_info_helping(response,search_term)
                page_parser_bandh(link)
    else:
        print("We are sorry! The item you looking for is not in the B&H store")
