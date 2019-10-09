from bs4 import BeautifulSoup
import requests
import re
from json_io import *

# getting the info from the website.
def wesite_bh_info_helping(response):
    soup = BeautifulSoup(response, 'lxml')
    price = soup.find_all('span', class_="itc-you-pay-price bold")
    item_brand = soup.find_all('span', itemprop="brand")
    item_name = soup.find_all('span', itemprop="name")
    for i in range(len(price)):
        print(item_brand[i].text + " " + item_name[i].text + " " + price[i].text)




# get the response and convert it into lxml format.
def wesite_bh_info(link):
    # list that will store all the link needed
    link_list = []

    # Opening the pages and check how many page numbers
    response = requests.get(link, headers=user_agent, allow_redirects=True).text
    soup = BeautifulSoup(response, 'lxml')
    if soup.find('div', class_="pagination-zone") == None:
       wesite_bh_info_helping(response)
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
            wesite_bh_info_helping(response)
