
class Anomaly():
    # Generic Anomaly in Space.
    def __init__(self, anomalieInformation):
        self.name = anomalieInformation['name']

        self.coordinates = anomalieInformation['coordinates']


class Planet(Anomaly):
    # Buy and Sell Goods
    def __init__(self, planetInformation):
        Anomaly.__init__(self, planetInformation)

        self.goodsConsumed = planetInformation['goodsConsumed']
        self.goodsProduced = planetInformation['goodsProduced']

        self.prices = planetInformation['prices']


class Starbase(Anomaly):
    # Buy Ships and Rooms
    def __init__(self, starbaseInformation):
        Anomaly.__init__(self, starbaseInformation)

        self.shipForSale = None

        self.roomsForSale = dict()

    def changeShipForSale(self, Ship):
        self.shipForSale = Ship

    def addRoomForSale(self, Room):
        self.roomsForSale.update({Room.name: Room})


class Spacegate(Anomaly):
    # Jump Anywhere for lower travel Cost
    def __init__(self, spacegateInformation):
        Anomaly.__init__(self, spacegateInformation)

        self.costForUse = spacegateInformation['costForUse']

    def overrideDistances(self):
        for dest in self.distances:
            self.distances[dest] = 1
