# Contains Ship Data


# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats - Dict Or Direct Assign? -> Go For Direct
        # self.stats = shipStats

        self.cargoCapacity = shipStats['cargoCapacity']
        self.speed = shipStats['speed']
        self.maxTravelDistance = shipStats['maxTravelDistance']

        # Price
        self.price = shipStats['price']

        # Rooms
        self.rooms = dict()
        self.spaceForRooms = shipStats['spaceForRooms']

        # Initialize Cargobay
        self.inCargo = dict()
        self.freeCargoSpace = shipStats['cargoCapacity']

        # Initialize SensorBay
        self.distances = dict()
        self.travelCosts = dict()

    # Room Operations
    def attachRoom(self, Room):
        self.rooms.update({Room.name: Room})

        Room.powerUp(self)

    def detachRoom(self, Room):
        Room.powerDown(self)

        del self.rooms[Room.name]

    # CargoBay Methods
    def loadCargo(self, cargoId, cargoAmount):
        if cargoId in self.inCargo:
            self.inCargo[cargoId] += cargoAmount
        else:
            self.inCargo.update({cargoId: cargoAmount})

        self.freeCargoSpace -= cargoAmount

    def unloadCargo(self, cargoId, cargoAmount):
        self.inCargo[cargoId] -= cargoAmount
        if self.inCargo[cargoId] <= 0:
            del self.inCargo[cargoId]

        self.freeCargoSpace += cargoAmount

    # Sensor Bay Methods
    def scanSector(self):
        # init travelCost Dict
        travelCostDict = dict()
        nearestDestination = None

        # Loop through Destinations
        for destination in self.distances:
            # Add if in Travel Distance
            if self.distances[destination] <= self.maxTravelDistance:
                travelCost = int(self.distances[destination] / self.speed)
                travelCostDict.update({destination: travelCost})

            # update nearest
            if not nearestDestination:
                nearestDestination = destination
            elif self.distances[destination] <= self.distances[nearestDestination]:
                if self.distances[destination] != 0.0:
                    nearestDestination = destination

        # Check For Reachable Destinations
        if len(travelCostDict) < 2:
                travelCost = int(self.distances[nearestDestination] / self.speed)
                travelCostDict.update({nearestDestination: travelCost})

        # update travelCosts
        self.travelCosts = travelCostDict


# Freighter. Can be overloaded.
class Freighter(Ship):
    def __init__(self, shipStats):
        # Assign Basic Stats
        Ship.__init__(self, shipStats)

        # Assign Special Stats
        self.overloadbonus = shipStats['overloadbonus']
        self.overloadmalus = shipStats['overloadmalus']

    def startOverload(self):
        self.cargoCapacity += self.overloadbonus
        self.speed -= self.overloadmalus

    def overloadEnd(self):
        self.cargoCapacity -= self.overloadbonus
        self.speed += self.overloadmalus
