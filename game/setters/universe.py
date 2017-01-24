import helpers.logger as log


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
        self._harbors.Set(harbor)
