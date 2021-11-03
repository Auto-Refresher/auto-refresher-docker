import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

depopURL = "https://www.depop.com"
user = "/harrywmo"
page = requests.get(depopURL + user)

driver = webdriver.Chrome('./chromedriver')

# Scrape individual items
def getProductNames():
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.select('a[data-testid="product__item"]')
    for item in items:
        print(item['href'][9:])
    return items

productPages = getProductNames()
driver.get(depopURL + 'edit' + productPages[0])

