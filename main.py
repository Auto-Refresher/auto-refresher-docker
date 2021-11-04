import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

depopURL = "https://www.depop.com"
user = "/harrywmo"
page = requests.get(depopURL + user)

print("Refreshing for: " + user)

driverURL = "http://web-chrome:4444"

def establishDriverConnection():
    while True:
        try:
            print("Attempting to establish Driver connection: ", driverURL)
            driver = webdriver.Remote(command_executor = driverURL)
        except:
            continue
        else:
          break
    print("Connected to Webdriver")
    return driver
       
        
#driver = webdriver.Chrome(service=s)
driver = establishDriverConnection()
print("Using " + driver.name)

# Scrape individual items
def getProductNames():
    products = []
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.select('a[data-testid="product__item"]')
    for item in items:
        if len(item.select('div[data-testid="product__sold"]')) == 0:
            products.append(item['href'][9:])
    return products

def getLoginCookies(page):
    with open("creds" + user + "/cookies.data", "r") as a_file:
        driver.get(depopURL + '/products/deit' + page)
        for line in a_file:
            stripped_line = line.strip()
            cookie = stripped_line.split(" ", 1)
            driver.add_cookie({"name" : cookie[0], "value" : cookie[1], "path" : "/", "domain": ".depop.com"})

getLoginCookies(getProductNames()[0])

def refreshItem(item):

    print("Refreshing Item: " + item)

    driver.get(depopURL + '/products/edit' + item)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    saveButton = driver.find_element_by_xpath('//button[text()="Save changes"]')
    
    saveButton.click()

    print(item + " refreshed!")

def refreshAll():
    # Refresh Items
    for product in getProductNames():
        refreshItem(product)
    
    print("Closing WebDriver")
    driver.close()
    print("Closed")

refreshAll()