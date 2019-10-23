# Functions to facilitate webscraping and data collection

# Usage Notes
    # The page_parser functions should be given the src of an html request, not the link. The request must
    # already be made prior to calling a page_parser function.


# Notes
    # Future Websites to consider
        # Microsoft, Apple, Dell, HP
    # Amazon switched up their HTML attributes on us, so I had to adapt to that with conditional statements
    # For me (Steven), Bestbuy has proven to disagree with my method for connecting to their website. Ali faces no similar issue.

    #  Walmart a bunch of prices nested in similar elements, but the first one listed is the current price.
    # B and H, as far as single item page goes, was fairly straight forward.
from bs4 import BeautifulSoup
<<<<<<< HEAD
from database_accessor import *
import requests
import os, sys
from json_io import user_agent

headers = user_agent
=======
import requests
from database_accessor import insertOneIntoResultTable
>>>>>>> c142308dd8f6c5396a17182bc97d1c32477eaaed

referer = "https://google.com"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'referer': referer
    }

# ========

# Search Page Parsing Functions
def search_parser_bestbuy(data):
    print("Nothing")


def search_parser_walmart(data):
    print("Nothing")


def search_parser_amazon(data):
    print("Nothing")


def search_parser_bandh(data):
    print("Nothing")

# ===================================
# Functions for parsing the actual product pages

# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_bestbuy(link):
    result = requests.get(link, headers=headers, timeout=None, allow_redirects=True)

    print(result.status_code)

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # Item Name
    # <div class="sku-title" itemprop="name">
    #  <h1 class="heading-5 v-fw-regular">"The Juice"</h1>
    # </div>
    tag = soup.find('div', {"class": "sku-title"})
    item_name = tag.h1.get_text()
    print(item_name)

    # Image Link
    # <img draggable="false" class="primary-image zoomable" src="thejuice">

    tag = soup.find('img', {"class": "primary-image"})
    image_link = tag["src"]
    print(image_link)

    # Brand
    tags = soup.find_all('div', {"class": "category-wrapper row"})
    for x in tags:
        if x.div.h3.get_text() == "General":
            parent_tag = x
            break
    specs_table = parent_tag.find('div', {"class": "specs-table col-xs-9"})
    ul = specs_table.ul.find_all('li')
    for x in ul:
        y = x.find('div', {"class": "title-container col-xs-6 v-fw-medium"})
        z = y.find('div', {"class": "row-title"})
        if z.get_text().strip() == "Brand":
            row = x
            break

    brand = row.find('div', {"class": "row-value col-xs-6 v-fw-regular"}).get_text()
    print(brand)

    # Price
    tag = soup.find('div', {"class": "priceView-hero-price priceView-customer-price"})
    price = tag.span.get_text().strip("$")
    print(price)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "Best Buy"}

    insertOneIntoResultTable(result)


# @pre  A query has been made and an http request has returned html to parse
# @post  The item price will be parsed and returned in an acceptable form
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_walmart(link):
    result = requests.get(link, headers=headers, stream=False)
    print(result.status_code)

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # Item Name
    tag = soup.find('h1', {"class": "prod-ProductTitle font-normal"})
    item_name = tag.get_text()
    print(item_name)

    # Brand
    tag = soup.find('span', {"itemprop": "brand"})
    brand = tag.get_text()
    print(brand)

    # Image Link
    tag = soup.find('img', {"class": "hover-zoom-hero-image"})
    image_link = tag["src"]
    print(image_link)

    # Price Acquisition
    # price-characteristic: the dollars
    # price-mantissa: the cents
    t_char = soup.select_one(".price-characteristic")
    print(t_char)

    t_mant = soup.select_one(".price-mantissa")
    print(t_mant)

    # Motive: Combine corresponding values from Price Char with Price Mantissa
    # The first value is the current price (or sale price)
    # The second one is a value hidden from display
    # The third value is the regular price
    price = t_char.get_text() + '.' + t_mant.get_text()

    print(price)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "Walmart"}

    insertOneIntoResultTable(result)


# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_amazon(link):
    result = requests.get(link, headers=headers, stream=False, allow_redirects=True)

    print(result.status_code)

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # For amazon
    # <span id="price_inside_buybox> value </span>
    # Get Item Name
    tag = soup.find('span', {"id": "productTitle"})
    item_name = tag.get_text(strip="true")
    print(item_name)

    # Get Brand Name
    tag = soup.find('a', {"id": "bylineInfo"})
    brand = tag.get_text()
    print(brand)

    # Get Image Link
    tag = soup.find('img', {"id": "landingImage"})
    image_link = tag['src']
    print(image_link)

    # Get price
    tag = soup.select("#price_inside_buybox")
    print(len(tag))
    if len(tag) == 0:
        print("Other")
        tag = soup.select("#priceblock_ourprice")
    price = tag[0].get_text(strip="true").strip("$")
    print(price)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "Amazon"}

    insertOneIntoResultTable(result)


# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_bandh(link):
    result = requests.get(link, headers=headers, timeout=None)

    print(result.status_code)

    src = result.content

    soup = BeautifulSoup(src, 'lxml')

    # Price
    tag = soup.find('div', {"data-selenium": "pricingPrice"})
    price = tag.get_text().strip('$')
    print(price)

    # Item Name
    tag = soup.find('h1', {"data-selenium": "productTitle"})
    item_name = tag.get_text()
    print(item_name)

    # Image Link
    tag = soup.find('img', {"data-selenium": "inlineMediaMainImage"})
    image_link = tag["src"]
    print(image_link)

    # Brand
    tag = soup.find('img', {"data-selenium": "authorizeDealerBrandImage"})
    brand = tag["alt"]
    print(brand)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "B&H"}

    insertOneIntoResultTable(result)
