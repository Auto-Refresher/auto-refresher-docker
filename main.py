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
    products = []
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.select('a[data-testid="product__item"]')
    for item in items:
        products.append(item['href'][9:])
    return products

productPages = getProductNames()

def getLoginCookies():
    with open("cookies.data", "r") as a_file:
        driver.get(depopURL + '/products/deit' + productPages[1])
        for line in a_file:
            stripped_line = line.strip()
            cookie = stripped_line.split(" ", 1)
            print("cookies in line:")
            print("name: ", cookie[0], "val: ", cookie[1])
            driver.add_cookie({"name" : cookie[0], "value" : cookie[1], "path" : "/", "domain": ".depop.com"})

getLoginCookies()
driver.get(depopURL + '/products/edit' + productPages[0])
driver.page_source.encode("utf-8")