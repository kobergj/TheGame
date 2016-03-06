import Queue


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

    def update(self, Universe):
        # Get Enemy from Queue
        newEnemy = Universe.enemyQ.get()
        # Append to Enemy List
        if newEnemy:
            self.enemies.append(newEnemy)


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
        self.roomsForSale = dict()

    def changeShipForSale(self, Ship):
        if self.shipForSale:
            # Attach to List Of Deprecated Ships
            self.deprecatedShips.append(self.shipForSale)

            del self.shipForSale

        # Attach Ship
        self.shipForSale = Ship

    def addRoomForSale(self, Room):
        self.roomsForSale.update({Room.name: Room})

    def update(self, Universe):
        Anomaly.update(self, Universe)

        # Get Ship
        ship = Universe.shipQ.get()

        # Attach Ship to Station
        self.changeShipForSale(ship)

        # Fill Room List
        while len(self.roomsForSale) < self.maxRoomsForSale:
            # Get Room
            room = Universe.roomQ.get()

            # Add Room
            self.addRoomForSale(room)


class Spacegate(Anomaly):
    # Jump Anywhere for lower travel Cost
    def __init__(self, spacegateInformation):
        Anomaly.__init__(self, spacegateInformation)

        self.costForUse = spacegateInformation['costForUse']

        self.travelCostDict = {}

    def updateTravelCostDict(self, anomalyList):
        # Loop through Anomalies
        for anomalyName in anomalyList:
            # Only Append if not there
            if anomalyName not in self.travelCostDict:
                # Update
                self.travelCostDict.update({anomalyName: 0})

    def update(self, Universe):
        # Update Anomaly
        Anomaly.update(self, Universe)

        # Update TravelCostDict
        self.updateTravelCostDict(Universe.anomalyList.keys())
