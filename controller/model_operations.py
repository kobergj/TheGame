
class BuyGood:
    def __init__(self, good, amount=1):
        self.good = good
        self.amount = amount

    def __call__(self, universe, player):
        player.currentShip.loadCargo(self.good, self.amount)

        player.spendCredits(self.good.price)

class TravelTo:
    def __init__(self, coordinates, distance):
        self.destination = coordinates

        self.distance = distance

    def __call__(self, universe, player):
        engine, energycore = player.currentShip.access_content('engine', 'energycore')

        energy_costs = engine(self.distance)

        energycore(energy_costs)

        player.travelTo(self.destination)

class Fight:
    """Basic Class for Fights"""
    def __init__(self, enemy):
        weapon, energycore = enemy.access_content('weapon', 'energycore')

        if int(energycore) >= weapon():
            self.enemy_action = self.attack

        else:
            self.enemy_action = self.recharge

    def __call__(self, universe, player):
        anomaly = universe[player.currentPosition]

        enemy = anomaly.enemies[0]

        # Player First
        self.player_action(player.currentShip, enemy)

        if not enemy.wreck():
            # Then Enemy
            self.enemy_action(enemy, player.currentShip)

    @staticmethod
    def attack(attacker, defender):
        wpn, core = attacker.access_content('weapon', 'energycore')

        shd = defender.access_content('shield')

        energy_costs = wpn()

        core(energy_costs)

        shd(int(wpn))

    @staticmethod
    def recharge(ship, _):
        core = ship.access_content('energycore')

        core()

class Attack(Fight):
    def __init__(self, enemy):
        Fight.__init__(self, enemy)

        self.player_action = self.attack

class Recharge(Fight):
    def __init__(self, enemy):
        Fight.__init__(self, enemy)

        self.player_action = self.recharge

class Flee(Fight):
    def __call__(self, universe, player):
        pass

class Pass:
    def __init__(self):
        pass

    def __call__(self, universe, player):
        pass



## Deprecates

class Fight_Player:
    def __call__(self, universe, player):
        anomaly = universe[player.currentPosition]

        enemy = anomaly.enemies[0]

        pl_wpn, pl_shd, pl_core = player.currentShip.access_content('weapon', 'shield', 'energycore')

        en_wpn, en_shd, en_core = enemy.access_content('shield')

        # Player First
        energy_costs = pl_wpn()

        pl_core(energy_costs)

        en_shd(int(pl_wpn))

        if int(en_shd) <= 0:
            return

        # Now Enemy


