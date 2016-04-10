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

        # Power Engines
        self.maxTravelDistance = cont.Stat(shipStats['maxTravelDistance'])
        self.maintenanceCosts = cont.Stat(shipStats['maintenanceCosts'])

        # Load Weapons
        self.attackPower = cont.Stat(shipStats['attackPower'])

        # activate Shields
        self.shieldStrength = cont.Stat(shipStats['shieldStrength'])

        # Rooms & Goods
        self.rooms = list()
        self.inCargo = dict()

    # Room Operations
    def attachRoom(self, Room):
        self.rooms.append(Room)

        self.spaceForRooms.addBoost(-1)

        for statBoost in Room.statBoosts:
            statBoost(self)

        Room.active = True

    def detachRoom(self, Room, remove=False):
        for statBoost in Room.statBoosts:
            statBoost.remove(self)

        Room.active = False

        if remove:
            self.rooms.remove(Room)

    # CargoBay Methods
    def loadCargo(self, cargo, cargoAmount=1):
        if cargo.name in self.inCargo:
            self.inCargo[cargo.name] += cargoAmount
        else:
            self.inCargo.update({cargo.name: cargoAmount})

        self.cargoCapacity.addBoost(cargoAmount*-1)

    def unloadCargo(self, cargo, cargoAmount=1):
        self.inCargo[cargo.name] -= cargoAmount
        if self.inCargo[cargo.name] <= 0:
            del self.inCargo[cargo.name]

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
        # self.enemyType = enemyStats['Fraction']

        # Loot
        self.lootableCredits = 0

    def addMoreCredits(self, Amount):
        self.lootableCredits += Amount
