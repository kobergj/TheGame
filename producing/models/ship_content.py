
class Room():
    def __init__(self, roomInformation):
        self.name = roomInformation['name']

        self.price = roomInformation['price']

        self.statBoosts = self.generateBoostList(roomInformation['statBoosts'])

        self.active = False

    def generateBoostList(self, statBoostInfoList):
        boostTypeDict = {
            'cargoCapacity':        CargoBoost,
            'maintenanceCosts':     MaintBoost,
            'attackPower':          AttackBoost,
            'shieldStrength':       ShieldBoost,
            'maxTravelDistance':    DistanceBoost,
        }

        boostList = list()

        for boostInfo in statBoostInfoList:
            statName = boostInfo[0]
            statValue = boostInfo[1]

            boost = boostTypeDict[statName](statValue)

            boostList.append(boost)

        return boostList


# The Cargo Bay contains Goods
# class CargoBay():
#     def __init__(self):
#         self.goodsList = list()

#     def load(self, Good):
#         self.goodsList.append(Good)

    # def unload(self, Good):
    #     for good in goodsList:
    #         if good.name == Good.name:
    #             self.goodsList.remove(Good)


class Good():
    def __init__(self, Info):
        self.name = Info['name']

        self.price = 0


    def changePrice(self, NewPrice):
        self.price = NewPrice


# Class For Stats
class Stat():
    def __init__(self, StartValue=0):
        # The Value of the Stat
        self.startValue = StartValue
        # Space for boosts
        self.boosts = list()
        # Free Space For Mocking
        self.tempValue = None

    def __call__(self):
        # Returns Current Value
        value = self.startValue

        for boost in self.boosts:
            value += boost

        return value

    def addBoost(self, Value):
        # Calculate inverted Value
        invertedValue = Value * -1
        # If inverted Value already present
        if invertedValue in self.boosts:
            # Remove It
            self.boosts.remove(invertedValue)
            return

        # Append Boost
        self.boosts.append(Value)

    def reset(self):
        self.boosts = []

    def increment(self, Value):
        self.startValue += Value

    # def decrease(self, Value):
    #     self.startValue -= Value

    def mock(self, TempValue):
        # Save Current
        self.tempValue = self.startValue
        # Mock
        self.startValue = TempValue

    def demock(self):
        if self.tempValue:
            # Give Value Back
            self.startValue = self.tempValue
            # Remove temp Value
            self.tempValue = None


# Method For Inverting a Stat Temporaly
class Invert():
    def __init__(self, ShipStat):
        self.stat = ShipStat

    def __enter__(self):
        self.stat.mock(self.stat.startValue * -1)

    def __exit__(self, type, value, traceback):
        self.stat.demock()


# StatBoosts
class StatBoost(Stat):
    # It has a Name
    statName = 'No Name'

    def __call__(self, Ship):
        # Get Corresponding Stat
        stat = self.correspondingStat(Ship)
        # Raise some Stat
        stat.increment(self.startValue)

    def correspondingStat(self, Ship):
        # Returns the Corresponding Stat
        pass

    def revert(self, Ship):
        # Get Stat
        stat = self.correspondingStat(Ship)
        # Revert
        stat.increment(self.startValue*-1)


# Boosts Cargo Capacity
class CargoBoost(StatBoost):
    statName = 'Cargo Capacity'
    def correspondingStat(self, Ship):
        return Ship.cargoCapacity

# Boosts Max Travel Dist
class DistanceBoost(StatBoost):
    statName = 'Max Travel Distance'
    def correspondingStat(self, Ship):
        return Ship.maxTravelDistance

# Boosts maintenance Costs
class MaintBoost(StatBoost):
    statName = 'Maintenance Costs'
    def correspondingStat(self, Ship):
        return Ship.maintenanceCosts

# Boosts Attack Power
class AttackBoost(StatBoost):
    statName = 'Attack'
    def correspondingStat(self, Ship):
        return Ship.attackPower

# Boosts Shield Strength
class ShieldBoost(StatBoost):
    statName = 'Defense'
    def correspondingStat(self, Ship):
        return Ship.shieldStrength
