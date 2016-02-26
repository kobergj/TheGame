
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
        # Init Anomaly
        Anomaly.__init__(self, starbaseInformation)

        # Ship Bay
        self.shipForSale = None
        self.shipPrice = 0

        # Room Merchant
        self.maxRoomsforSale = starbaseInformation['maxRoomsforSale']
        self.roomsForSale = dict()

    def changeShipForSale(self, Ship):
        # Attach Ship
        self.shipForSale = Ship
        # Calculate Costs
        self.calculateShipPrice(Ship)

    def addRoomForSale(self, Room):
        # Add Room
        self.roomsForSale.update({Room.name: Room})

    def calculateShipPrice(self, Ship):
        price = 0
        for statValue in Ship.stats.values():
            price += statValue

        price *= 10

        self.shipPrice = price


class Spacegate(Anomaly):
    # Jump Anywhere for lower travel Cost
    def __init__(self, spacegateInformation):
        Anomaly.__init__(self, spacegateInformation)

        self.costForUse = spacegateInformation['costForUse']

    def overrideDistances(self):
        for dest in self.distances:
            self.distances[dest] = 1
