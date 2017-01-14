import helpers.logger as log


class UniverseViewer:
    def __init__(self, universe):
        self._universe = universe
        self._harborViewer = HarborViewer(universe.harbors)

    def CurrentHarborCargo(self):
        for c in self._harborViewer.GetCargoList():
            price = 0  # Some price Interface Magic
            yield c, price

    def CurrentHarborName(self):
        return self._harborViewer.Name()

    def Destinations(self, amount):
        return self._harborViewer.Destinations()


class HarborViewer:
    def __init__(self, harbors):
        self._harbors = harbors

    def Name(self):
        return self._current().name

    @log.Logger('Get Cargo List')
    def GetCargoList(self):
        return list(iter(self._current().cargo))

    def Destinations(self, amount):
        return self._harbors.LookUp(amount)

    def _current(self):
        return self._harbors.Current()
