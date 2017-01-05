import models as m
import container as c

import random

SAMPLECARGO = ["Sample Cargo", "Another Cargo"]
SAMPLEHARBORS = ["Safe Harbor", "Even safer Harbor"]


def SampleHarborFactory():
    cf = CargoFactory(*SAMPLECARGO)

    return HarborFactory(cf, *SAMPLEHARBORS)


class HarborFactory:
    def __init__(self, cargofactory, *harbornames):
        self.harbornames = harbornames
        self.cargofactory = cargofactory

    def RandomHarbor(self):
        name = random.choice(self.harbornames)

        pricefactory = PriceFactory([5, 10])

        num = random.randint(1, 4)
        cargocontainer = c.Container()
        for cargo in self.cargofactory.RandomCargoList(num):
            cargocontainer + cargo

        return m.Harbor(name, cargocontainer, pricefactory)


class CargoFactory:
    def __init__(self, *cargonames):
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
