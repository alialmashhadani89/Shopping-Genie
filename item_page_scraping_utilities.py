# Functions to facilitate webscraping and data collection

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


    soup = BeautifulSoup(data, 'lxml')
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
    t_comb = t_char.get_text() + '.' + t_mant.get_text()

    print(t_comb)
    return t_comb

# A helper function for filtering
def filter_whitespace(string):
    for x in string:
        if x >= '0' and x <= '9' or x == '.':
            return True
        else:
            return False

# @pre
# @post
# @param  data  The source/html of an http request to a particular item page
# @return  The price of a single item, in $.00 format
def page_parser_amazon(data):
    # Amazon requires some extra filtering due to how their information is displayed.
    #

    soup = BeautifulSoup(data, 'lxml')

    # For amazon
    # <span id="price_inside_buybox> value </span>
    tag = soup.select("#price_inside_buybox")
    print(len(tag))
    if (len(tag) == 0):
        print("Other")
        tag = soup.select("#priceblock_ourprice")
    listVal = list(filter(filter_whitespace, tag[0].get_text()))
    price = ''.join(str(e) for e in listVal)
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
