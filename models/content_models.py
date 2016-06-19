import random


class ShipContent:
    def __init__(self, name, capacity=0, energycosts=0):
        self.name = name

        self._encost = Stat(energycosts)

        self._cap = Stat(capacity)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def costs(self, *informations):
        return int(self.energy_costs)


class Weapon(ShipContent):
    def __init__(self, attack_range, ap_costs):
        ShipContent.__init__(self, 'weapon', attack_range[0], ap_costs)

        self._maxcap = Stat(attack_range[1])

    def fire(self):
        return int(self._cap), int(self._maxcap)

class Engine(ShipContent):
    def __init__(self, maxtraveldist, encosts):
        ShipContent.__init__(self, 'engine', maxtraveldist, encosts)

    def max_distance(self):
        return int(self._cap)

class Shield(ShipContent):
    def __init__(self, maxstrength, energycosts):
        ShipContent.__init__(self, 'shield', maxstrength, energycosts)

class EnergyCore(ShipContent):
    def __init__(self, max_energy, refillrate):
        ShipContent.__init__(self, 'energycore', max_energy, refillrate)

class CargoBay(ShipContent):
    def __init__(self, size, energycosts=0):
        ShipContent.__init__(self, 'cargobay', size, energycosts)

        self.cargo_list = list()

    def amount(self, good):
        return map(str, self.cargo_list).count(str(good))

    def load(self, good):
        self.cargo_list.append(good)

    def unload(self, good_to_unload):
        for i, good in enumerate(self.cargo_list):
            if good == good_to_unload:
                self.cargo_list.pop(i)
                return

    def free_space(self):
        return self.size - len(self.cargo_list)

    def full(self):
        return self.free_space() <= 0


class Good(ShipContent):
    def __init__(self, name, price=0):
        ShipContent.__init__(self, name)

        self.price = price

    def changePrice(self, NewPrice):
        self.price = NewPrice


class Room(ShipContent):
    def __init__(self, roomInformation):

        ShipContent.__init__(self, roomInformation['name'])


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


# Class For Stats
class Stat:
    def __init__(self, StartValue=0, MaxStartValue=None):
        # The Value of the Stat
        self.startValue = StartValue
        # Max Value
        self.maxstartValue = MaxStartValue
        # Space for boosts
        self.boosts = list()
        # Max Boosts
        self.maxboosts = list()
        # Free Space For Mocking
        self.tempValue = None

    def __call__(self):
        # Returns Current Value
        value = self.startValue

        for boost in self.boosts:
            value += boost

        if self.maxstartValue:

            maxvalue = self.maxstartValue

            for boost in self.maxboosts:
                maxvalue += boost

            return value, maxvalue

        return value

    def __int__(self):
        # Returns Current Value
        value = self.startValue

        for boost in self.boosts:
            value += boost

        if self.maxstartValue:

            maxvalue = self.maxstartValue

            for boost in self.maxboosts:
                maxvalue += boost

            return value, maxvalue

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
class Invert:
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

# Boosts Action Points
class EnergyBoost(StatBoost):
    statName = 'Action Points'
    def correspondingStat(self, ship):
        return ship.energy

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
