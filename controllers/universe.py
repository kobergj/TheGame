import implementations.factory as fac

PRICERANGE = [5, 14]


class UniverseController:
    def __init__(self, universe):
        self._universe = universe
        self._harborfactory = fac.HarborFactory(universe.harbornames)
        self._cargofactory = fac.CargoFactory(universe.cargonames)

        self.SwitchHarbor(self.NewHarbor())

    def SwitchHarbor(self, harbor):
        self._currentHarbor = harbor

    def GetHarbor(self):
        return self._currentHarbor

    def NewHarbor(self):
        return self._harborfactory.RandomHarbor(self._cargofactory)


class HarborController:
    def __init__(self, harbor):
        self._harbor = harbor

    def IterateCargo(self):
        for cargo in self._harbor.cargo:
            yield cargo


class PriceController:
    def __init__(self):
        self._priceFactory = fac.PriceFactory(PRICERANGE)

    def __call__(self, item):
        return self._priceFactory.RandomPrice(item)
