import models as m
import container as c

import random


class HarborFactory:
    def __init__(self, harbornames):
        self.harbornames = harbornames

    def RandomHarbor(self, cargofactory):
        name = random.choice(self.harbornames)

        num = random.randint(1, 4)
        cargocontainer = c.Container()
        for cargo in cargofactory.RandomCargoList(num):
            cargocontainer + cargo

        return m.Harbor(name, cargocontainer)


class CargoFactory:
    def __init__(self, cargonames):
        self.cargonames = cargonames

    def RandomCargo(self):
        name = random.choice(self.cargonames)
        cargo = m.Cargo(name)
        return cargo

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
