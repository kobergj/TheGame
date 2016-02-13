# Contains Ship Data


# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats
        self.cargoCapacity = shipStats['cargoCapacity']
        self.speed = shipStats['speed']
        self.maxTravelDistance = shipStats['maxTravelDistance']

        # Initialize Cargobay
        self.inCargo = dict()
        self.freeCargoSpace = shipStats['cargoCapacity']

        # Initialize SensorBay
        self.distances = dict()
        self.travelCosts = dict()

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
    def scanSector(self, distanceDict):
        # update distances
        self.distances = distanceDict

        # calculate travelCosts
        travelCostDict = dict()
        for destination in self.distances:
            if self.distances[destination] <= self.maxTravelDistance:
                travelCost = int(self.distances[destination] / self.speed)
                travelCostDict.update({destination: travelCost})

        # update travelCosts
        self.travelCosts = travelCostDict

    # Deprecated
    # def initSectorMap(self):
    #     # Currently Two Dimensional.

    #     sectorMap = list()
    #     for j in range(self.maxTravelDistance*2):
    #         row = list()
    #         for i in range(self.maxTravelDistance*2):
    #             row.append(0)
    #         sectorMap.append(row)

    # # Not Sure if this right here.
    # def updateSectorMap(self, relativeCoordinatesDict):
    #     # Currently Two Dimensional.
    #     self.sectorMap = self.initSectorMap()

    #     self.sectorMapLegend = ['Nothing']
    #     i = 1
    #     for anomaly in relativeCoordinatesDict:
    #         cords = relativeCoordinatesDict[anomaly]
    #         if cords[0] in range(self.maxTravelDistance*2):
    #             if cords[1] in range(self.maxTravelDistance*2):
    #                 self.sectorMap[cords[1]][cords[0]] = i
    #                 self.sectorMapLegend.append(anomaly)
    #                 i += 1


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
