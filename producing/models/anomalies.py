
class Anomaly():
    # Generic Anomaly in Space.
    def __init__(self, anomalieInformation):
        # Identifier
        self.name = anomalieInformation['name']
        # Coordinates
        self.coordinates = None
        # Enemies in Orbit
        self.enemies = list()

    def addEnemy(self, enemy):

        self.enemies.append(enemy)

    def getCoordinates(self, Coordinates):
        self.coordinates = Coordinates


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
        self.deprecatedShips = list()

        # Room Merchant
        self.maxRoomsForSale = starbaseInformation['maxRoomsforSale']
        self.roomsForSale = list()

    def changeShipForSale(self, Ship):
        if self.shipForSale:
            # Attach to List Of Deprecated Ships
            self.deprecatedShips.append(self.shipForSale)

            del self.shipForSale

        # Attach Ship
        self.shipForSale = Ship

    def addRoomForSale(self, Room):
        self.roomsForSale.append(Room)


class Spacegate(Anomaly):
    # Jump Anywhere for lower travel Cost
    def __init__(self, spacegateInformation):
        Anomaly.__init__(self, spacegateInformation)

        self.costForUse = spacegateInformation['costForUse']

        self.travelDistance = 99

        self.playersMaxTravelDist = None
