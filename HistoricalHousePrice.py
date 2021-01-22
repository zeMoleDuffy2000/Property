
class HistoricalHousePrice:
    """A sample property class"""

    def __init__(self, price, date):
        self.price = price
        self.date = date

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date