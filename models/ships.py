# Contains Ship Data


# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats
        self.cargoCapacity = shipStats['cargoCapacity']
        self.speed = shipStats['speed']

        # Initialize Cargobay
        self.inCargo = dict()
        self.freeCargoSpace = shipStats['cargoCapacity']

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
