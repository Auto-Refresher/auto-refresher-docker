import requests
from bs4 import BeautifulSoup

URL = "https://www.depop.com/harrywmo/"
page = requests.get(URL)

# Scrape individual items
soup = BeautifulSoup(page.content, "html.parser")
items = soup.select('a[data-testid="product__item"]')
for item in items:
    print(item)



