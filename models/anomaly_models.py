
# class Anomaly():
#     # Generic Anomaly in Space.
#     def __init__(self, name, enemies=list()):
#         # Identifier
#         self.name = name
#         # Coordinates
#         self.coordinates = None
#         # Enemies in Orbit
#         self.enemies = enemies
#         # Enemy Graveyard
#         self.dead_enemies = list()
#         # Cost To Get here
#         self.travelCosts = None

#     def addEnemy(self, enemy):
#         self.enemies.append(enemy)

#     def killEnemy(self, enemyindex=0):
#         enemy = self.enemies.pop(enemyindex)

#         self.dead_enemies.append(enemy)

#     def getCoordinates(self, Coordinates):
#         self.coordinates = Coordinates

#     def setTravelCosts(self, value):
#         self.travelCosts = value


# class Planet(Anomaly):
#     # Buy and Sell Goods
#     def __init__(self, name, enemies=list(), goods=list()):
#         Anomaly.__init__(self, name)

#         # self.goodsConsumed = goodsconsumed
#         # self.goodsProduced = goodsproduced

#         self.goods = goods

#     def addGood(self, good):
#         self.goodsConsumed.append(good)


# class Starbase(Anomaly):
#     # Buy Ships and Rooms
#     def __init__(self, name, maxRoomsforSale=3):
#         # Init Anomaly
#         Anomaly.__init__(self, name)

#         # Ship Bay
#         self.shipForSale = None
#         self.deprecatedShips = list()

#         # Room Merchant
#         self.maxRoomsForSale = maxRoomsforSale
#         self.roomsForSale = list()

#     def changeShipForSale(self, Ship):
#         if self.shipForSale:
#             # Attach to List Of Deprecated Ships
#             self.deprecatedShips.append(self.shipForSale)

#             del self.shipForSale

#         # Attach Ship
#         self.shipForSale = Ship

#     def addRoomForSale(self, Room):
#         self.roomsForSale.append(Room)

#     def remove_room(self, room):
#         for avail_room in self.roomsForSale:
#             if avail_room.name == room.name:
#                 room_to_remove = avail_room 

#         self.roomsForSale.remove(room_to_remove)

# class Spacegate(Anomaly):
#     # Jump Anywhere for lower travel Cost
#     def __init__(self, name, costForUse=0):
#         Anomaly.__init__(self, name)

#         self.costForUse = costForUse

#         self.travelDistance = 99

#         self.playersMaxTravelDist = None



## TESTING SECTION ###

class Anomaly:
    def __init__(self, name, anomalytype='Anomaly', enemies=list(), goods=None,
                    jumpgatecosts=None, rooms=None):

        self.name = name
        self.anomalytype = anomalytype
        # Coordinates
        self.coordinates = None
 
        self.orbit = _Orbit(enemies)

        if goods is not None:
            self.merchant = _Merchant(goods)

        if jumpgatecosts is not None:
            self.jumpgate = _JumpGate(jumpgatecosts)

        if rooms is not None:
            self.eqdealer = _EqDealer(rooms)

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def killEnemy(self, enemyindex=0):
        enemy = self.enemies.pop(enemyindex)

        self.dead_enemies.append(enemy)

    def getCoordinates(self, Coordinates):
        self.coordinates = Coordinates

    def setTravelCosts(self, value):
        self.travelCosts = value


class _Merchant:
    def __init__(self, goods=list()):
        self._goods = goods

    def add_good(self, good):
        self._goods.append(good)

    def show_stock(self, descending=False):
        return sorted(self._goods, key=lambda x: x.price, reverse=descending)

class _JumpGate:
    def __init__(self, costforuse=0):
        self._costforuse = costforuse

    def show_price(self):
        return int(self._costforuse)

class _EqDealer:
    def __init__(self, rooms):
        self._rooms = rooms

class _Orbit:
    def __init__(self, enemies=list()):
        self._enemies = enemies
        self._deadenemies = list()

    def __iter__(self):
        return iter(self._enemies)

    def get_enemy(self):
        return self._enemies[0]

    def add_enemy(self, enemy):
        self._enemies.append(enemy)

    def remove_enemy(self, enemyindex=0):
        enemy = self._enemies.pop(enemyindex)
        self._deadenemies.append(enemy)

    def empty(self):
        return len(self._enemies) == 0

