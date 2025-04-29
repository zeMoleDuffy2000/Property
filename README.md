Overview

This project is a Python application that scrapes historical property sale prices from government and real estate websites. It stores the data in a local SQLite database and visualizes year-over-year property value trends for a specific street.
The project was designed to analyze hyperlocal property market trends and understand value growth over time.

Features

Web scraping with Selenium to collect property sales data.
SQLite database creation and querying to manage scraped data.
Data cleaning and organization using pandas.
Visualization of price trends using matplotlib.
Object-oriented design for managing property-related data.

Technologies Used

Python 3
Selenium
pandas
matplotlib
SQLite3
NumPy

How to Run

Install Python 3.
Install required libraries: selenium, pandas, matplotlib, numpy.
Download ChromeDriver and add it to your system PATH.
Clone this repository.
Run 'createStreetDataBase.py' or 'app.py' to start the data scraping and database creation process.
A graph showing year-over-year property prices will be generated.

Project Structure

createStreetDataBase.py: Scrapes property sale data and stores it in SQLite.
app.py: Alternate version of data scraping and visualization.
GraphStreetDataBase.py: Graphs the historical data stored in SQLite.
PropertyData.py, LandRegPropertyData.py, HistoricalHousePrice.py: Classes for structured property data management.

Author

Philip O'Duffy LinkedIn: https://www.linkedin.com/in/poduffy/ GitHub: https://github.com/zeMoleDuffy2000
