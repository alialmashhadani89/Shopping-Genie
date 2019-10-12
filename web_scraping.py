from bs4 import BeautifulSoup
import requests
import re
from json_io import *


def check_item(item_brand,item_name,search_term):
    if search_term.find('\"') == -1:
        index_of_tilt = str(item_name[0].text).find('\"') + 1
        full_item_name = str(item_brand[0].text).lower() + str(item_name[0].text).lower()[index_of_tilt:]
        print(full_item_name)
        print(search_term)
        if str(search_term).lower() in full_item_name:
            return True
        else:
            return False
    else:
        full_item_name =  str(item_brand[0].text).lower() + " " + str(item_name[0].text).lower()
        if str(search_term).lower() in full_item_name:
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
def wesite_bh_info_helping(response,search_term):
    soup = BeautifulSoup(response, 'lxml')
    price = soup.find_all('span', class_="itc-you-pay-price bold")
    item_brand = soup.find_all('span', itemprop="brand")
    item_name = soup.find_all('span', itemprop="name")
    images = soup.find_all('img', {'src':re.compile('.jpg')})
    price_index = 0
    for i in range(len(price)):
        if check_item(item_brand,item_name,search_term):
            print(item_brand[i].text + " " + item_name[i].text + " " + price[i].text + " " + images[i] ['src'])




# get the response and convert it into lxml format.
def wesite_bh_info(link,search_term):
    # list that will store all the link needed
    link_list = []

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')

    # if the item in the store, we will go forth with the search.
    # if not then we will stop the search.
    if search_guard(response,search_term):

        if soup.find('div', class_="pagination-zone") == None:
           wesite_bh_info_helping(response,search_term)
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
                wesite_bh_info_helping(response,search_term)
    else:
        print("We are sorry!The item you looking for is not in the B&H store")
