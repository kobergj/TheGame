import producing.models.ship_content as cont

# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Stats
        # Price
        self.price = cont.Stat(shipStats['price'])

        # Rooms
        self.spaceForRooms = cont.Stat(shipStats['spaceForRooms'])

        # Initialize Cargobay
        self.cargoCapacity = cont.Stat(shipStats['cargoCapacity'])
        self.freeCargoSpace = cont.Stat(shipStats['cargoCapacity'])

        # Power Engines
        self.maxTravelDistance = cont.Stat(shipStats['maxTravelDistance'])
        self.maintenanceCosts = cont.Stat(shipStats['maintenanceCosts'])

        # Load Weapons
        self.attackPower = cont.Stat(shipStats['attackPower'])

        # activate Shields
        self.shieldStrength = cont.Stat(shipStats['shieldStrength'])

        # Testing Stats
        self.rooms = list()
        self.inCargo = dict()
        # self.CargoBay = self.cont.CargoBay()
        # self.HappyCargoCap = ShipStat(shipStats['cargoCapacity'])

    # Room Operations
    def attachRoom(self, Room):
        self.rooms.append(Room)

        self.spaceForRooms.addBoost(-1)

        for statBoost in Room.statBoosts:
            statBoost(self)

    def detachRoom(self, Room):
        Room.powerDown(self)

        self.rooms.remove(Room)

    # CargoBay Methods
    def loadCargo(self, cargoId, cargoAmount):
        if cargoId in self.inCargo:
            self.inCargo[cargoId] += cargoAmount
        else:
            self.inCargo.update({cargoId: cargoAmount})

        self.cargoCapacity.addBoost(cargoAmount*-1)

    def unloadCargo(self, cargoId, cargoAmount):
        self.inCargo[cargoId] -= cargoAmount
        if self.inCargo[cargoId] <= 0:
            del self.inCargo[cargoId]

        self.cargoCapacity.addBoost(cargoAmount)


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


# Enemy
class Enemy(Ship):
    def __init__(self, enemyStats):
        # Assign Basic Stats
        Ship.__init__(self, enemyStats)

        # Enemy Type
        self.enemyType = enemyStats['Fraction']

        # Loot
        self.credits = enemyStats['creditStash']


