# Contains Ship Data


# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats - Dict Or Direct Assign? -> Go For Direct
        # self.stats = shipStats

        # Price
        self.price = shipStats['price']

        # Rooms
        self.rooms = dict()
        self.spaceForRooms = shipStats['spaceForRooms']

        # Initialize Cargobay
        self.cargoCapacity = shipStats['cargoCapacity']
        self.inCargo = dict()
        self.freeCargoSpace = shipStats['cargoCapacity']

        # Initialize SensorBay
        self.distances = dict()
        self.travelCosts = dict()

        # Power Engines
        self.maxTravelDistance = shipStats['maxTravelDistance']
        self.speed = shipStats['speed']

        # Load Weapons
        self.attackPower = shipStats['attackPower']

        # activate Shields
        self.shieldStrength = shipStats['shieldStrength']

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
    def scanSector(self, distances):
        # init travelCost Dict
        travelCostDict = dict()
        nearestDestination = None

        # Loop through Destinations
        for destination, distance in distances.iteritems():
            # Check if in Travel Distance
            if distance <= self.maxTravelDistance:
                # Calculate Costs
                travelCost = int(distance / self.speed)
                # Update Dict
                travelCostDict.update({destination: travelCost})

            # update nearest - There is surely a better way for this
            if not nearestDestination:
                nearestDestination = destination

            elif distance <= distances[nearestDestination]:
                if distance != 0.0:
                    nearestDestination = destination

        # Check For Reachable Destinations
        if len(travelCostDict) < 2:
                travelCost = int(distances[nearestDestination] / self.speed)
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
