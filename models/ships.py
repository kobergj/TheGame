# Contains Ship Data


# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats - Dict Or Direct Assign?
        self.stats = shipStats

        self.cargoCapacity = shipStats['cargoCapacity']
        self.speed = shipStats['speed']
        self.maxTravelDistance = shipStats['maxTravelDistance']

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

        Room.attachAt(self)

    def detachRoom(self, Room):
        Room.detachFrom(self)

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
        # calculate travelCosts
        travelCostDict = dict()
        for destination in self.distances:
            if self.distances[destination] <= self.maxTravelDistance:
                travelCost = int(self.distances[destination] / self.speed)
                travelCostDict.update({destination: travelCost})

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
