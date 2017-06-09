import requests
from bs4 import BeautifulSoup

# Tickets to be searched throughout the different online vendors
def concert_tickets(item_url):
	url = "https://www.stubhub.com/florida-georgia-line-tickets-florida-georgia-line-wantagh-northwell-health-at-jones-beach-theater-6-15-2017/event/9806266/?mbox=1&rS=6&abbyo=true&sliderpos=false&qtyq=false&qtyddab=true&sort=price+asc"
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
	for item_name in soup.findAll('div', {'class': 'dollar-value'}):
		div = item_name.get('div')
		print(item_name.string)

# Call the function for testing
concert_tickets(div)

