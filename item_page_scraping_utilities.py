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
def page_parser_bestbuy(data):
    # For the time being, as far as I am aware, Bestbuy is being difficult. Thus, havent actually tested this yet
    soup = BeautifulSoup(data, 'lxml')

    tag = soup.select(".priceView-hero-price")
    print(tag)




# @pre  A query has been made and an http request has returned html to parse
# @post  The item price will be parsed and returned in an acceptable form
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_walmart(data):
    # To be noted that Walmart apparently splits up the price into two pieces, and has
    # several prices listed on the page (with regards to sales, regular price, financing, etc)
    # Thus I've elected to assemble a list of these prices, and we can figure out what to do with them
    # at a later time.

    # I have discovered the magic of soup.select_one(), and am using it to pull the first option.

    # Product title
    # <h1 class="prod-productTitle font-normal" content="Apple Airpods" itemprop="name">Apple Airpods</h1>

    # Brand Name
    # <span itemprop="brand">Apple</span>

    # Product Image
    # <div class="hover-zoom-hero-image-container">
    #   <img class="hover-zoom-hero-image" src="thejuice">
    # </div>



    soup = BeautifulSoup(data, 'lxml')

    # Item Name
    tag = soup.find('h1', {"class": "prod-ProductTitle font-normal"})
    item_name = tag.get_text()
    print(item_name)

    # Brand
    tag = soup.find('span', {"itemprop": "brand"})
    brand_name = tag.get_text()
    print(brand_name)

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
    return price

# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_amazon(data):
    # Amazon  requires some extra filtering due to how their information is displayed.

    # Price
    # <span id="price_inside_buybox> value </span>

    # Product name
    # <span id="productTitle class="a-size-large">
    #   " <A whole lot of whitespace, then> ASUS Chromebook modelnumber details and specs"
    # </span>

    # Image(s?)
    # <div id="imgTagWrapperId" class="imgTagWrapper" style="height: 443px;">
    #   <img alt="itemname/desc" src="the juice" ~~ id="landingImage" ~~~~ >
    # </div>



    soup = BeautifulSoup(data, 'lxml')

    # Get Item Name
    tag = soup.find('span', {"id": "productTitle"})
    item_name = tag.get_text(strip="true")
    print(item_name)

    # Get Brand Name
    tag = soup.find('a', {"id": "bylineInfo"})
    brand_name = tag.get_text()
    print(brand_name)

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
    price = tag[0].get_text(strip="true")

    print(price)
    return price


# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_bandh(data):
    # <div class="price_1DPoToKrLP8uWvruGqgtaY" data-selenium="pricingPrice">$904.48</div>
    #
    soup = BeautifulSoup(data, 'lxml')
    tag = soup.find('div', {"data-selenium": "pricingPrice"})
    value = tag.get_text().strip('$')

    return value
