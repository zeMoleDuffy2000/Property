# figure out how to rewrite data table entry to pass in real address
# how to plot on a map with UI elements and functions like custom appearing boxes
#
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PropertyData import Property

import sqlite3 as sql
import re


conn = sql.connect('property.db')

# c = conn.cursor()

# try :
#     c.execute("""CREATE TABLE houses (
#                 address1 text,
#                 address2 text,
#                 desc text,
#                 link text,
#                 price integer,
#                 propertyType text,
#                 bedroomNo integer,
#                 bathroomNo integer,
#                 tenure text
#                 )""")
# except Exception:
#     print("houses table already exists")

# c.execute("INSERT INTO houses VALUES('Sharrow Lane, Sharrow', '5 bedroom detached house for sale', 150000, 'detached', 5, 1, 'Freehold')")


from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.rightmove.co.uk/")

search = driver.find_element_by_id("searchLocation")
search.send_keys("crookes")
search.send_keys(Keys.RETURN)


# propertyType = driver.find_element_by_id("displayPropertyType").click()

driver.find_element_by_xpath("//select[@name='displayPropertyType']/option[text()='Houses']").click()

driver.find_element_by_id("submit").click()

prop1 = Property("null","null","null",-1, "null",-1, -1, "null", "null")

# driver.get("https://www.rightmove.co.uk/properties/87486100#/streetView")

# output = driver.find_element_by_class_name("gm-iv-short-address-description")
# newAddressT = output.text + ', ' + driver.find_element_by_class_name("gm-iv-long-address-description").text
# print(newAddressT)

propertyCards = driver.find_elements_by_class_name("propertyCard-wrapper")
propertyLinks = []
for thing in propertyCards:
    # header = thing.find_element_by_class_name("propertyCard-title")
    # prop1.desc = header.text
    # prop1.desc
    header = thing.find_element_by_class_name("propertyCard-link")
    propertyLinks.append(header.get_attribute('href'))
    # print(header.text)
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL)
    # actions.click(header)
    # actions.key_up(Keys.CONTROL)
    # actions.perform()
    header = thing.find_element_by_class_name("propertyCard-address")
    prop1.address = header.text

    # print(header.text)

    # c.execute("INSERT INTO houses VALUES('Sharrow Lane, Sharrow', '5 bedroom detached house for sale', 150000, 'detached', 5, 1, 'Freehold')")

# driver.close()

for propertyLink in propertyLinks:
    # print(propertyLink)
    driver.get(propertyLink)
    driver.refresh()
    prop1.link = propertyLink
    # def scrapeRMPageEntry():
    # driver.get("https://www.rightmove.co.uk/properties/87486100#/")


    # priceResult = driver.find_element_by_xpath("//main/div[1]/div[1]/div/div/div/span").text
    try:
        priceResult = driver.find_element_by_xpath("//main/div[2]/div[2]/div[1]/div[1]").text
    except Exception:
        priceResult = driver.find_element_by_xpath("//main/div[2]/div[1]/div[1]/div[1]").text

    s = priceResult
    formattedPrice = re.sub("[^0-9|.]", "", s)  # 123456.79
    prop1.price = formattedPrice
    print("prop1.price = " + prop1.price)

    try:
        bedroomResults = driver.find_element_by_xpath("//main/div[5]/div[2]/div[2]/div[2]").text
    except Exception:
        print("prop1.bedroomNo = 0")
        # try:
        #     print(driver.find_element_by_xpath("//main/div[5]/div[2]/").text)
        # except Exception:
        #     print("ouch")
        # print("opsEnd")
        # # print(driver.find_element_by_xpath("//main/").text)
        # # bedroomResults = None
    else:
        s = bedroomResults
        prop1.bedroomNo = re.sub("[^0-9|.]", "", s)  # 123456.79
        print('prop1.bedroomNo = ' + prop1.bedroomNo)

    try:
        bathroomResults = driver.find_element_by_xpath("//main/div[5]/div[3]/div[2]/div[2]").text
    except Exception:
        print("prop1.bathroomNo = 0")
        # print(driver.find_element_by_xpath("//main/").text)
        # bedroomResults = None
    else:
        s = bathroomResults
        prop1.bathroomNo = re.sub("[^0-9|.]", "", s)  # 123456.79
        print('prop1.bathroomNo = ' + prop1.bathroomNo)



    driver.find_element_by_xpath("//a[@href='#/streetView']").click()
    # newAddress = driver.find_element_by_xpath("//h1[@class='widget-titlecard-header']")
    # newAddress = driver.find_element_by_xpath("//div[@class='gm-iv-short-address-description']")
    driver.refresh()
    try:
        newAddress = driver.find_element_by_class_name("gm-iv-short-address-description")
    except Exception:
        print("bad shit")
    else:
        prop1.address1 = newAddress.text
        print(prop1.address1)

    try:
        newAddress2 = driver.find_element_by_class_name("gm-iv-long-address-description")
    except Exception:
        print("bad shit")
    else:
        prop1.address2 = newAddress2.text
        print(prop1.address2)

    # newAddressT = newAddress.text + driver.find_element_by_class_name("gm-iv-long-address-description").text
    # print(newAddress.text)

    c.execute("INSERT INTO houses VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(prop1.address1, prop1.address2, prop1.desc, prop1.link, prop1.price, prop1.propertyType, prop1.bedroomNo, prop1.bathroomNo, prop1.tenure))
    print("----------------")

c.execute("SELECT * FROM houses")
print(c.fetchall())
# scrapeRMPageEntry()

# driver.get("https://landregistry.data.gov.uk/app/ppd")
# driver.find_element_by_id("street").send_keys("Steade" + Keys.RETURN)
# # driver.find_element_by_class_name("button").click()
#
# # items = driver.find_elements_by_tag_name("li")
# items = driver.find_elements_by_xpath("//ul[@class='list-unstyled ppd-results']/li")
# for item in items:
#     text = item.text
#     print(text)

 #c.execute("SELECT * FROM houses")
# dbEntries = c.fetchall()
# for entry in dbEntries:
#     print(entry)
#     driver.get(entry[2])
#     driver.find_element_by_xpath("//a[@href='#/streetView']").click()
#     # newAddress = driver.find_element_by_xpath("//h1[@class='widget-titlecard-header']")
#     # newAddress = driver.find_element_by_xpath("//div[@class='gm-iv-short-address-description']")
#     newAddress = driver.find_elements_by_class_name("gm-iv-short-address-description")
#     newAddressT = newAddress.text + driver.find_elements_by_class_name("gm-iv-long-address-description").text
#     print(newAddress.text)
#     entry[2] = newAddress.text


 # print(c.fetchall())


conn.commit()
conn.close()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
#
#
# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')


# if __name__ == "__main__":
#     driver.run(debug=True, host="0.0.0.0", port=80)
