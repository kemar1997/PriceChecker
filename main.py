import requests
from bs4 import BeautifulSoup
import sys


# from update_api import _to_ascii

# div = item_name.get('div')

# Tickets to be searched throughout the different online vendors
# Defining the initial product
def concert_tickets():
    url = "https://www1.ticketmaster.com/chance-the-rapper-tampa-florida-06-14-2017/event/0D005246C6439730?artistid=1750234&majorcatid=10001&minorcatid=3&tm_link=artist_msg-0_0D005246C6439730"
    source_code = requests.get(url)
    plain_text = source_code.text.encode(sys.stdout.encoding,
                                         errors='replace')
   # print(plain_text)
    soup = BeautifulSoup(plain_text, "html.parser")
    # try:
    for price_info in soup.findAll('span'):
        button = price_info.get('span')
        # print(partials)
       # print(button)
        print(price_info)
    # except UnicodeEncodeError:
    #	pass


# Call the function for testing
# _to_ascii('\xa9')
concert_tickets()
