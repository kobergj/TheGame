import models.models as m
import helpers.logger as log

import random


class HarborFactory:
    def __init__(self, harbornames, cargofactory):
        self.harbornames = harbornames
        self.cargofactory = cargofactory

    @log.Logger('Random Harbor')
    def RandomHarbor(self):
        name = random.choice(self.harbornames)

        num = random.randint(1, 4)
        cargocontainer = list()
        for cargo in self.cargofactory.RandomCargoList(num):
            item = [cargo, 1]
            cargocontainer.append(item)

        return m.Harbor(name, cargocontainer)


class CargoFactory:
    def __init__(self, cargonames):
        self.cargonames = cargonames

    @log.Logger('Random Cargo')
    def RandomCargo(self):
        name = random.choice(self.cargonames)
        cargo = m.Cargo(name)
        return cargo

    @log.Logger('Random Cargo List')
    def RandomCargoList(self, length):
        for _ in range(length):
            yield self.RandomCargo()


class PriceFactory:
    def __init__(self, pricerange):
        self.pricerange = pricerange

    def RandomPrice(self, cargo):
        return random.randint(*self.pricerange)


class PlayerFactory:
    def __init__(self, *playernames):
        self.playernames = playernames

    def RandomPlayer(self):
        name = random.choice(self.playernames)
        return m.Player(name)


class SpaceFactory:
    def __init__(self, *args):
        self.args = args

    def RandomSpace(self):
        return m.Space()
