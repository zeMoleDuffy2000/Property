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

street = "Archer Road"



conn = sqlite3.connect('{}.db'.format(street))
quoteStreet = "'"+street+"'"
query = 'SELECT * FROM {}'.format(quoteStreet)
print(query)
df = pd.read_sql(query, conn)


print("printing DF")
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)

print("Storing DF into Database")

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
    if i > 1:
        print("adding plot number {}".format(i))

        formattedHousePriceSeries = df.iloc[:, i].dropna()

        formattedHousePricesList = df.iloc[:, i].tolist()
        floatFormattedHousePrice = [float(item) for item in formattedHousePricesList]
        print("floatFormattedHousePrice before na")
        print(floatFormattedHousePrice)
        print(type(floatFormattedHousePrice))

        series1 = np.array(floatFormattedHousePrice).astype(np.double)
        print("series1")
        print(series1)
        mask = series1 > 0.0
        plt.plot(npDates[mask], series1[mask], linestyle='-', marker='o')
        print("floatFormattedHousePrice after na")
        print(floatFormattedHousePrice)

    i += 1

# plt.gca().invert_yaxis()
houseLegend = []

for col in df.columns:
    if col != "index" and col != "Year":
        houseLegend.append(col)

plt.legend(houseLegend)
plt.gcf().autofmt_xdate()
plt.show()



conn.commit()
conn.close()

