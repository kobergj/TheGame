
class Anomaly():
    # Generic Anomaly in Space.
    def __init__(self, name):
        # Identifier
        self.name = name
        # Coordinates
        self.coordinates = None
        # Enemies in Orbit
        self.enemies = list()
        # Enemy Graveyard
        self.dead_enemies = list()
        # Cost To Get here
        self.travelCosts = None

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def killEnemy(self, enemyindex=0):
        enemy = self.enemies.pop(enemyindex)

        self.dead_enemies.append(enemy)

    def getCoordinates(self, Coordinates):
        self.coordinates = Coordinates

    def setTravelCosts(self, value):
        self.travelCosts = value


class Planet(Anomaly):
    # Buy and Sell Goods
    def __init__(self, name):
        Anomaly.__init__(self, name)

        self.goodsConsumed = list()
        self.goodsProduced = list()

        # self.prices = planetInformation['prices']

    def raiseConsume(self, good):
        self.goodsConsumed.append(good)

    def raiseProducing(self, good):
        self.goodsProduced.append(good)


class Starbase(Anomaly):
    # Buy Ships and Rooms
    def __init__(self, name, maxRoomsforSale=3):
        # Init Anomaly
        Anomaly.__init__(self, name)

        # Ship Bay
        self.shipForSale = None
        self.deprecatedShips = list()

        # Room Merchant
        self.maxRoomsForSale = maxRoomsforSale
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

    def remove_room(self, room):
        for avail_room in self.roomsForSale:
            if avail_room.name == room.name:
                room_to_remove = avail_room 

        self.roomsForSale.remove(room_to_remove)

class Spacegate(Anomaly):
    # Jump Anywhere for lower travel Cost
    def __init__(self, name, costForUse=0):
        Anomaly.__init__(self, name)

        self.costForUse = costForUse

        self.travelDistance = 99

        self.playersMaxTravelDist = None
