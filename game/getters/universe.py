import helpers.logger as log


class UniverseViewer:
    def __init__(self, universe):
        self._universe = universe
        self._harborViewer = HarborViewer(universe.harbors)

    def CurrentHarborCargo(self):
        return self._harborViewer.GetCargoList()

    def CurrentHarborName(self):
        return self._harborViewer.Name()

    def Destinations(self, amount):
        return self._harborViewer.Destinations(amount)


class HarborViewer:
    def __init__(self, harbors):
        self._harbors = harbors

    def Name(self):
        return self._current().name

    @log.Logger('Get Cargo List')
    def GetCargoList(self):
        for cargo in self._current().cargo:
            yield cargo

    def Destinations(self, amount):
        return self._harbors.LookUp(amount)

    def _current(self):
        return self._harbors.Current()
