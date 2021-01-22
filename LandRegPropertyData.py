
class LandRegPropertyData:
    """A sample property class"""

    def __init__(self, address1, propertyType, tenure, link):
        self.address1 = address1
        self.propertyType = propertyType
        self.tenure = tenure
        self.link = link
        self.historicalHousePrice = []

    def addHistoricalPrice(self, HistoricalPrice):
        self.historicalHousePrice.append(HistoricalPrice)

    def getHistoricalPrice(self):
        return self.historicalHousePrice