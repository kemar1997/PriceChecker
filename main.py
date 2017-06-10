import requests 
from bs4 import BeautifulSoup

# div = item_name.get('div')

# Tickets to be searched throughout the different online vendors
# Defining the initial product
def concert_tickets():
	url = "https://www.stubhub.com/florida-georgia-line-tickets-florida-georgia-line-wantagh-northwell-health-at-jones-beach-theater-6-15-2017/event/9806266/?mbox=1&rS=6&abbyo=true&sliderpos=false&qtyq=false&qtyddab=true&sort=price+asc"
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
	for price_info in soup.findAll('div', {'class': 'partials'}):
		div = prince_info.get('div')
		#dollar-value = price_info.string
		partials = price_info.string
		#print(partials)
		print(soup)
		print(price_info)
# Call the function for testing
concert_tickets()

