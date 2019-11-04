# Functions to facilitate webscraping and data collection

from bs4 import BeautifulSoup
import requests
from json_io import user_agent
from database_accessor import insertOneIntoResultTable
headers = user_agent
referer = "https://google.com"

# ===================================
# Functions for parsing the actual product pages

def bestbuy_brand_table_parser(tags):
    brand_in_general = False

    for x in tags:
        if x.div.h3.get_text() == "General":
            general_tag = x
            break
    specs_table = general_tag.find('div', {"class": "specs-table col-xs-9"})
    ul = specs_table.ul.find_all('li')
    for x in ul:
        y = x.find('div', {"class": "title-container col-xs-6 v-fw-medium"})
        z = y.find('div', {"class": "row-title"})
        if z.get_text().strip() == "Brand":
            brand_in_general = True
            row = x
            break

    if brand_in_general:
        return row
    else:
        brand_in_other = False
        for x in tags:
            if x.div.h3.get_text() == "Other":
                other_tag = x
                break
        specs_table = other_tag.find('div', {"class": "specs-table col-xs-9"})
        ul = specs_table.ul.find_all('li')
        for x in ul:
            y = x.find('div', {"class": "title-container col-xs-6 v-fw-medium"})
            z = y.find('div', {"class": "row-title"})
            if z.get_text().strip() == "Brand":
                other_in_general = True
                row = x
                break
        return row


# @pre  A search result page has been scraped of any links for items relevant to the search
# @post  A valid result will be inserted into the database.
# @param  link  The link of the item page to be scraped.
def page_parser_bestbuy(link):
    #print(link)
    result = requests.get(link, headers=headers, timeout=None, allow_redirects=True)

    #print(result.status_code)

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # Item Name
    tag = soup.find('div', {"class": "sku-title"})
    item_name = tag.h1.get_text()
    #print(item_name)


    tag = soup.find('img', {"class": "primary-image"})
    image_link = tag["src"]
    #print(image_link)

    # Brand
    tags = soup.find_all('div', {"class": "category-wrapper row"})
    row = bestbuy_brand_table_parser(tags)

    brand = row.find('div', {"class": "row-value col-xs-6 v-fw-regular"}).get_text()
    #print(brand)

    # Price
    tag = soup.find('div', {"class": "priceView-hero-price priceView-customer-price"})
    if tag == None:
        print("Item is no longer available")
        return
    pre_price = tag.span.get_text()
    if pre_price == None:
        # Problem
        print("Item no longer available")
        return False
    else:
        price = pre_price.strip("$").replace(",","")
    #print(price)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "Best Buy"}

    insertOneIntoResultTable(result)
    return True

# @pre  A website's search result page has been scraped of any item page links relevant to the search
# @post  A result, if valid, will be inserted into the database
# @param  link  The link of the item page to be scraped.
def page_parser_walmart(link):
    result = requests.get(link, headers=headers, stream=False)
    #print("Walmart Item Scraper")
    #print(result.status_code)
    #print(link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # Item Name
    tag = soup.find('h1', {"class": "prod-ProductTitle font-normal"})
    item_name = tag.get_text()
    #print(item_name)

    # Brand
    tag = soup.find('span', {"itemprop": "brand"})
    brand = tag.get_text()
    #print(brand)

    # Image Link
    tag = soup.find('img', {"class": "hover-zoom-hero-image"})
    if tag == None:
        tag = soup.find('img', {"class": "prod-hero-image-image"})
    image_link = tag["src"]
    #print(image_link)

    # Price Acquisition
    # price-characteristic: the dollars
    # price-mantissa: the cents
    t_char = soup.select_one(".price-characteristic")
    #print(t_char)

    t_mant = soup.select_one(".price-mantissa")
    #print(t_mant)

    # Motive: Combine corresponding values from Price Char with Price Mantissa
    # The first value is the current price (or sale price)
    # The second one is a value hidden from display
    # The third value is the regular price
    price = t_char.get_text().replace(",","") + '.' + t_mant.get_text()

    #print(price)

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
# @param  link  The link of the item page to be scraped
def page_parser_amazon(link):
    result = requests.get(link, headers=headers, stream=False, allow_redirects=True)
    prelink = result.url
    link = prelink[0:prelink.index("/ref=")]

    #print(result.status_code)
    #print(link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # For amazon
    # <span id="price_inside_buybox> value </span>
    # Get Item Name
    tag = soup.find('span', {"id": "productTitle"})
    item_name = tag.get_text(strip="true")
    #print(item_name)

    # Get Brand Name
    tag = soup.find('a', {"id": "bylineInfo"})
    brand = tag.get_text()
    #print(brand)

    # Get Image Link
    tag = soup.find('img', {"id": "landingImage"})
    image_link = tag['data-old-hires']
    #print("Image Link")
    #print(image_link)

    # Get price
    tag = soup.select("#price_inside_buybox")
    if len(tag) == 0:
        print("Other")
        tag = soup.select("#priceblock_ourprice")

    if len(tag) == 0:
        return False
    price = tag[0].get_text(strip="true").strip("$").replace(',', '')
    print(price)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "Amazon"}

    insertOneIntoResultTable(result)
    return True

# @pre  A search result page has been scraped of any links relevant to the search
# @post  A valid result will be inserted into the database
# @param  link  The link of the item page to scrape.
def page_parser_bandh(link):
    result = requests.get(link, headers=headers, timeout=None, allow_redirects=True)
    print(link)
    print(result.status_code)

    src = result.content

    soup = BeautifulSoup(src, 'lxml')
    #print(soup)

    # Price
    tag = soup.find('div', {"data-selenium": "pricingPrice"})
    if tag == None:
        return False
    price = tag.get_text().strip('$').replace(",","")
   # print(price)

    # Item Name
    tag = soup.find('h1', {"data-selenium": "productTitle"})
    item_name = tag.get_text()
    #print(item_name)

    # Image Link
    tag = soup.find('img', {"data-selenium": "inlineMediaMainImage"})
    image_link = tag["src"]
    #print(image_link)

    # Brand
    tag = soup.find('img', {"data-selenium": "authorizeDealerBrandImage"})
    if tag == None:
        tag = soup.find('a', {"data-selenium": "authorizedDealerLink"})
        brand = tag.span.get_text()
    else:
        brand = tag["alt"]
    #print(brand)

    result = {
        "price": price,
        "url": link,
        "item_name": item_name,
        "image_link": image_link,
        "brand": brand,
        "seller": "B&H"}

    insertOneIntoResultTable(result)
    return True