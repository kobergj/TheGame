import models as m

import random

SAMPLECARGO = ["Sample Cargo", "Another Cargo"]
SAMPLEHARBORS = ["Safe Harbor", "Even safer Harbor"]


def SampleHarborFactory():
    cf = CargoFactory(*SAMPLECARGO)

    return HarborFactory(cf, *SAMPLEHARBORS)


class CargoFactory:
    def __init__(self, *cargonames):
        self.cargonames = cargonames

    def RandomCargo(self):
        name = random.choice(self.cargonames)
        cargo = m.Cargo(name)
        return cargo


class HarborFactory:
    def __init__(self, cargofactory, *harbornames):
        self.harbornames = harbornames
        self.cargofactory = cargofactory

    def RandomHarbor(self):
        name = random.choice(self.harbornames)

        i = random.randint(1, 4)

        cargo = list()
        for _ in range(i):
            cargo.append(self.cargofactory.RandomCargo())

        return m.Harbor(name, cargo)
