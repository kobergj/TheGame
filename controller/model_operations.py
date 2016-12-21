
class BuyGood:
    def __init__(self, good, amount=1):
        self.good = good
        self.amount = amount

    def __call__(self, universe, player):
        if not self.good:
            return

        cargobay = player.currentShip.access_content('cargobay')

        cargobay.load(self.good, self.amount)

        price = self.good.price

        player.spendCredits(price)

        return

class SellGood(BuyGood):
    def __call__(self, universe, player):
        cargobay = player.currentShip.access_content('cargobay')

        cargobay.unload(self.good)

        price = self.good.price

        player.earnCredits(price)

        return

class EnterJumpgate:
    def __init__(self, price):
        self.price = price

    def __call__(self, universe, player):
        player.spendCredits(self.price)

        engine = player.currentShip.access_content('engine')

        engine.enter_hyperspace()

        return

class Travel:
    def __init__(self, coordinates, distance):
        self.destination = coordinates

        self.distance = distance

    def __call__(self, universe, player):
        engine, energycore = player.currentShip.access_content('engine', 'energycore')

        energy_costs = engine.costs(self.distance)

        energycore(energy_costs)

        player.travelTo(self.destination)

        engine.exit_hyperspace()

        universe.request_update = True

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


