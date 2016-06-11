import models.content_models as cont

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


    ### TESTING Section

    def TEST__init__(self, name, startcontent=list()):

        self.name = name

        self._content = list()

        for cnt in startcontent:
            self.change_content(cnt)

    def access_content(self, *contentnames):

        cnt_list = list()

        for contentname in contentnames:

            for cnt in self._content:
                if cnt.name == contentname:
                    cnt_list.append(cnt)

        return cnt_list

    def remove_content(self, contentname):
        for cnt in self._content:
            if cnt.name == contentname:
                self._content.remove(cnt)
                break

    def change_content(self, newcontent):
        self.remove_content(newcontent.name)

        self._content.append(newcontent)



    # Ship Methods

    def fire_weapon(self):
        if not self.weapon:
            return 0

        # Calc Energy Costs
        energycosts = int(self.weapon)
        # Spend Energy
        self.energycore(energycosts)
        # Calc Damage
        damage = self.weapon()

        return damage

    def suffer_damage(self, damage):
        if not self.shield:
            return

        self.shield(damage)

    def recharge_energy(self):

        self.energycore(None)

    def power_ftl(self, distance):
        # Calc E Costs
        energycosts = self.engine(distance)

        self.energycore(energycosts)


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
        self.lootableGoods = list()

    def addMoreCredits(self, Amount):
        self.lootableCredits += Amount

    def addMoreGoods(self, good):
        self.lootableGoods.append(good)
