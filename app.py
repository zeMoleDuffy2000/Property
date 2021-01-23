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
from LandRegPropertyData import LandRegPropertyData
from HistoricalHousePrice import HistoricalHousePrice
from matplotlib import pyplot as plt
from matplotlib import style
from datetime import datetime
import numpy as np
import pandas as pd
import inspect
import time

import sqlite3
import re

conn = sqlite3.connect('property.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE houses (
                address1 text,
                address2 text,
                desc text,
                link text,
                price integer,
                propertyType text,
                bedroomNo integer,
                bathroomNo integer,
                tenure text
                )""")
except Exception:
    print("houses table already exists")

# c.execute("INSERT INTO houses VALUES('Sharrow Lane, Sharrow', '5 bedroom detached house for sale', 150000, 'detached', 5, 1, 'Freehold')")


from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://landregistry.data.gov.uk/app/ppd")
# #
search = driver.find_element_by_id("street")
street = "tavistock road"
search.send_keys(street)

search = driver.find_element_by_id("town")
search.send_keys("sheffield")
search.send_keys(Keys.RETURN)

# date_time_str = '2018-06-29 08:15:27.243860'
#
# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#
# landRegProperty = LandRegPropertyData("123 road", "Terrace", "Freehold", "bla")
# historicalPropPrice = HistoricalHousePrice(160000, date_time_obj.date())
# landRegProperty.addHistoricalPrice(historicalPropPrice)
#
# date_time_str = '2020-06-29 08:15:27.243860'
# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
# historicalPropPrice = HistoricalHousePrice(200000, date_time_obj.date())
# landRegProperty.addHistoricalPrice(historicalPropPrice)
# landRegProperty.historicalHousePrice[0]
#
# x = [1,2,3]
# y = [1,4,9]
# plt.plot(x,y)
# plt.title(street)
# plt.xlabel("date")
# plt.ylabel("price")
#
# i = [3,3,4]
# j = [2,3,8]
# plt.plot(i, j)
#
# houseNumbers = []
# houseNumbers.append(1)
# houseNumbers.append(2)
# plt.legend(houseNumbers)
# plt.show()

# for i in inspect.getmembers(landRegProperty.historicalHousePrice[0]):
#     # to remove private and protected
#     # functions
#     if not i[0].startswith('_'):
#
#         # To remove other methods that
#         # doesnot start with a underscore
#         if not inspect.ismethod(i[1]):
#             print(i)


# length = len(landRegProperty.historicalHousePrice)
# i = 0
# while i < length:
#     date_time_str = landRegProperty.historicalHousePrice[i].date
#     date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#     print(date_time_obj.date())
#
#     i +=  1

# for thing in landRegProperty.getHistoricalPrice():
#     print(thing.)


# # propertyType = driver.find_element_by_id("displayPropertyType").click()
#
# driver.find_element_by_xpath("//select[@name='displayPropertyType']/option[text()='Houses']").click()
#
# driver.find_element_by_id("submit").click()
#
# prop1 = Property("null","null","null",-1, "null",-1, -1, "null", "null")
#
# # driver.get("https://www.rightmove.co.uk/properties/87486100#/streetView")
#
# # output = driver.find_element_by_class_name("gm-iv-short-address-description")
# # newAddressT = output.text + ', ' + driver.find_element_by_class_name("gm-iv-long-address-description").text
# # print(newAddressT)
#
# propertyCards = driver.find_elements_by_class_name("detailed-address")
# propertyCards = driver.find_elements_by_class_name("div[class='col-md-4 detailed-address']")
# propertyCards = driver.find_element_by_xpath("//a[@aria-label='add a filter for building name or&nbsp;number']")
propertyCards = driver.find_elements_by_css_selector("a[aria-label='add a filter for building name or&nbsp;number']")

df = pd.DataFrame()

print(len(propertyCards))
propertyLinks = []
for thing in propertyCards:
    print(thing.text)
    # subElement = thing.find_element_by_class_name("propertyCard-title")
    # prop1.desc = header.text
    # prop1.desc
    # header = thing.find_element_by_class_name("tbody")
    # propertyLink = thing.find_element_by_xpath("//tbody/tr[1]/td[2]/a[1]")
    # print(thing.find_element_by_xpath("//tbody/tr[1]/td[2]/a[1]"))
    # thing.find
    print("-----")
    link = thing.get_attribute('href')
    propertyLinks.append(link)
    print(link)
    print("-----")

    # propertyLinks.append(propertyLink.get_attribute('href'))
    # print(header.text)
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL)
    # actions.click(header)
    # actions.key_up(Keys.CONTROL)
    # actions.perform()
    # header = thing.find_element_by_class_name("propertyCard-address")
    # prop1.address = header.text
#
#     # print(header.text)
#
#     # c.execute("INSERT INTO houses VALUES('Sharrow Lane, Sharrow', '5 bedroom detached house for sale', 150000, 'detached', 5, 1, 'Freehold')")
#
# # driver.close()
#

propertyLink = propertyLinks[0]
pricePlot = []
datePlot = []
houseLegend = []

# initialise the data from first column
count = 0
i = 1920
defaultHousePriceList = {'Year': []}
while i < 2021:
    defaultHousePriceList['Year'].append(i)
    i += 1

# defaultHousePriceList = {}
# while i < 2021:
# #     # df[i] = [0]
#     defaultHousePriceList[i] = [0]
#     i += 1

df = pd.DataFrame(defaultHousePriceList)

# print("printing DF")
#
# print(df)

try:
    for propertyLink in propertyLinks:
        # initialise the current house column
        currentHousePriceList = {}

        j = 1920
        while j < 2021:
            currentHousePriceList[j] = 0
                # float('nan')
            # strOutput = "currentHousePriceList {} = {}"
            # print(strOutput.format(j, currentHousePriceList[j]))
            j += 1

        # print(currentHousePriceList)

        print(propertyLink)
        driver.get(propertyLink)
        driver.refresh()

        # prop1.link = propertyLink
        # def scrapeRMPageEntry():
        # driver.get("https://www.rightmove.co.uk/properties/87486100#/")

        # priceResult = driver.find_element_by_xpath("//main/div[1]/div[1]/div/div/div/span").text
        # print(driver.find_element_by_xpath("//div[@class = 'col-md-4 transaction-history']")
        transactionHistoryBlock = driver.find_element_by_xpath("//div[@class = 'col-md-4 transaction-history']")
        print("<transactionHistoryBlock>")
        print(transactionHistoryBlock.text)
        print("<transactionHistoryBlock>")
        # transactionHistories = transactionHistoryBlock.find_elements_by_xpath("//tr")
        transactionHistories = transactionHistoryBlock.find_elements_by_tag_name("tr")
        print(len(transactionHistories))
        print("<tranhistory>")

        for tranHistory in transactionHistories:
            tranRows = tranHistory.find_elements_by_tag_name("td")
            try:
                priceResult = tranRows[2].text
                s = priceResult
                formattedPrice = re.sub("[^0-9|.]", "", s)  # 123456.79
                pricePlot.append(formattedPrice)
                print("Price = " + formattedPrice)
            except:
                print("No Price")

            try:
                date_time_str = tranRows[1].text
                print("dateNoFormat = " + date_time_str)
                date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d")
                print(date_time_obj.year)
                datePlot.append(date_time_obj.year)

                currentHousePriceList[date_time_obj.year] = formattedPrice

            except:
                print("No Date")

        try:
            houseName = houseLegend.append(driver.find_element_by_class_name("address").text)
            print("legend = " + driver.find_element_by_class_name("address").text)

            df[driver.find_element_by_class_name("address").text] = df['Year'].map(currentHousePriceList)
        except:
            print("no legend")

        # count += 1
        #
        # if count == 2:
        #     print("breaking")
        #     break

        # plt.plot(datePlot, pricePlot, marker='.')
        # datePlot.clear()
        # pricePlot.clear()
        time.sleep(12)
except:
    print("something went wrong")

finally:

    print("printing DF")
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df)

    plt.title(street)

    plt.xlabel("date")
    plt.ylabel("price")
    style.use('dark_background')

    i = 0
    numberOfCols = len(df.columns)
    formattedhouseDates = df['Year'].tolist()
    print("formattedhouseDates")
    print(formattedhouseDates)
    npDates = np.array(formattedhouseDates)

    while i < numberOfCols:
        if i != 0:
            print("adding plot number {}".format(i))

            formattedHousePriceSeries = df.iloc[:, i].dropna()

            formattedHousePricesList = df.iloc[:, i].tolist()
            floatFormattedHousePrice = [float(item) for item in formattedHousePricesList]
            print("floatFormattedHousePrice before na")
            print(floatFormattedHousePrice)
            print(type(floatFormattedHousePrice))

            # i = 0
            # while i < len(floatFormattedHousePrice):
            #     if floatFormattedHousePrice[i] == 0.0:
            #         floatFormattedHousePrice[i] = None
            #     i += 1

            # for item in floatFormattedHousePrice :
            #     if floatFormattedHousePrice[item] == 0.0:
            #         floatFormattedHousePrice[item] = float('nan')
            series1 = np.array(floatFormattedHousePrice).astype(np.double)
            print("series1")
            print(series1)
            mask = series1 > 0.0
            plt.plot(npDates[mask], series1[mask], linestyle='-', marker='o')
            print("floatFormattedHousePrice after na")
            print(floatFormattedHousePrice)

        i += 1

    # plt.gca().invert_yaxis()
    plt.legend(houseLegend)
    print("<tranhistory/>")
    plt.gcf().autofmt_xdate()
    plt.show()

# try:
#     priceResult = driver.find_element_by_xpath("//main/div[2]/div[2]/div[1]/div[1]").text
# except Exception:
#     priceResult = driver.find_element_by_xpath("//main/div[2]/div[1]/div[1]/div[1]").text
#
# s = priceResult
# formattedPrice = re.sub("[^0-9|.]", "", s)  # 123456.79
# prop1.price = formattedPrice
# print("prop1.price = " + prop1.price)

# try:
#     bedroomResults = driver.find_element_by_xpath("//main/div[5]/div[2]/div[2]/div[2]").text
# except Exception:
#     print("prop1.bedroomNo = 0")
#     # try:
#     #     print(driver.find_element_by_xpath("//main/div[5]/div[2]/").text)
#     # except Exception:
#     #     print("ouch")
#     # print("opsEnd")
#     # # print(driver.find_element_by_xpath("//main/").text)
#     # # bedroomResults = None
# else:
#     s = bedroomResults
#     prop1.bedroomNo = re.sub("[^0-9|.]", "", s)  # 123456.79
#     print('prop1.bedroomNo = ' + prop1.bedroomNo)
#
# try:
#     bathroomResults = driver.find_element_by_xpath("//main/div[5]/div[3]/div[2]/div[2]").text
# except Exception:
#     print("prop1.bathroomNo = 0")
#     # print(driver.find_element_by_xpath("//main/").text)
#     # bedroomResults = None
# else:
#     s = bathroomResults
#     prop1.bathroomNo = re.sub("[^0-9|.]", "", s)  # 123456.79
#     print('prop1.bathroomNo = ' + prop1.bathroomNo)
#
#
#
# driver.find_element_by_xpath("//a[@href='#/streetView']").click()
# newAddress = driver.find_element_by_xpath("//h1[@class='widget-titlecard-header']")
# newAddress = driver.find_element_by_xpath("//div[@class='gm-iv-short-address-description']")

# try:
#     newAddress = driver.find_element_by_class_name("gm-iv-short-address-description")
# except Exception:
#     print("bad shit")
# else:
#     prop1.address1 = newAddress.text
#     print(prop1.address1)
#
# try:
#     newAddress2 = driver.find_element_by_class_name("gm-iv-long-address-description")
# except Exception:
#     print("bad shit")
# else:
#     prop1.address2 = newAddress2.text
#     print(prop1.address2)

# newAddressT = newAddress.text + driver.find_element_by_class_name("gm-iv-long-address-description").text
# print(newAddress.text)

# c.execute("INSERT INTO houses VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(prop1.address1, prop1.address2, prop1.desc, prop1.link, prop1.price, prop1.propertyType, prop1.bedroomNo, prop1.bathroomNo, prop1.tenure))
print("----------------")
#
# c.execute("SELECT * FROM houses")
# print(c.fetchall())
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

# c.execute("SELECT * FROM houses")
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
