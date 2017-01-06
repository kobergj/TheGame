import universe as u
import player as p


class LogicViewer:
    def __init__(self, player, universe):
        self._player = p.PlayerViewer(player)
        self._universe = u.UniverseViewer(universe)

    def CargoBuyOptions(self):
        for cargo in self._universe.ShowHarborCargo():
            price = 0  # self._priceInterface(cargo)
            yield cargo, price

    def __call__(self, logic):
        print 'Works'
        raw_input()
