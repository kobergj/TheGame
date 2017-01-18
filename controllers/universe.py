import helpers.logger as log


HARBORCONTROLLERCACHE = 5
DESTINATIONS = 3


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

    @log.Logger("Call Destination Controller")
    def Travel(self, harbor):
        t = True
        while t:
            for h in self._harbors.Get(DESTINATIONS):
                if h == harbor:
                    self._current = self._harbors.Current()
                    t = False
                    break
