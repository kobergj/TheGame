import implementations.factory as fac

PRICERANGE = [5, 14]


class UniverseController:
    def __init__(self, universe):
        self._universe = universe

    def Travel(self, harbor):
        con = self._universe.harbors
        for h, a in con:
            if a > 0:
                con - harbor

            if h == harbor:
                con + harbor


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
