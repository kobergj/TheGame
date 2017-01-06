
class UniverseViewer:
    def __init__(self, universe):
        self._universe = universe

    def GetCurrentHarbor(self):
        for h in self._universe:
            if self._universe[h] == 1:
                return h

    def ShowHarborCargo(self):
        h = self.GetCurrentHarbor()
        return h.cargo
