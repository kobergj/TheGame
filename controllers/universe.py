import implementations.factory as fac

PRICERANGE = [5, 14]
HARBORCONTROLLERCACHE = 5


class UniverseController:
    def __init__(self, universe):
        self._universe = universe

        self._destinationController = DestinationController(universe.harbors)

    def Travel(self, harbor):
        return self._destinationController.Travel(harbor)


class DestinationController:
    def __init__(self, harbors):
        self._harbors = harbors
        self._current = harbors.Current()

    def Travel(self, harbor):
        t = True
        while t:
            for h in self._harbors.Get():
                if h == harbor:
                    t = False


class PriceController:
    def __init__(self):
        self._priceFactory = fac.PriceFactory(PRICERANGE)

    def __call__(self, item):
        return self._priceFactory.RandomPrice(item)
