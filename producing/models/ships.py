

# Generic Ship. No special Abilites.
class Ship():
    def __init__(self, shipStats):
        # Assign Stats - Dict Or Direct Assign? -> Go For Direct
        # self.stats = shipStats

        # Price
        self.price = shipStats['price']

        # Rooms
        self.rooms = list()
        self.spaceForRooms = shipStats['spaceForRooms']

        # Initialize Cargobay
        self.cargoCapacity = shipStats['cargoCapacity']
        self.inCargo = dict()
        self.freeCargoSpace = shipStats['cargoCapacity']

        # # Initialize SensorBay
        # self.distances = dict()
        # self.travelCosts = dict()

        # Power Engines
        self.maxTravelDistance = shipStats['maxTravelDistance']
        self.maintenanceCosts = shipStats['maintenanceCosts']

        # Load Weapons
        self.attackPower = shipStats['attackPower']

        # activate Shields
        self.shieldStrength = shipStats['shieldStrength']

        # Testing Stats
        self.HappyCargoCap = ShipStat(shipStats['cargoCapacity'])

    # Room Operations
    def attachRoom(self, Room):
        self.rooms.append(Room)

        Room.powerUp(self)

    def detachRoom(self, Room):
        Room.powerDown(self)

        self.rooms.remove(Room)

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


# Class For Ship Stats
class ShipStat():
    def __init__(self, StartValue=0):
        # The Value of the Stat
        self.value = StartValue
        # Free Space For Mocking
        self.tempValue = None

    def __call__(self):
        return self.value

    def increment(self, Value):
        self.value += Value

    def decrease(self, Value):
        self.value -= Value

    def mock(self, TempValue):
        # Save Current
        self.tempValue = self.value
        # Mock
        self.value = TempValue

    def deMock(self):
        # Give Value Back
        self.value = self.tempValue
