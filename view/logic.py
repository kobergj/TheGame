import universe as u
import player as p


class LogicViewer:
    def __init__(self, player, universe):
        self._player = p.PlayerViewer(player)
        self._universe = u.UniverseViewer(universe)

    def CargoBuyOptions(self):
        for cargo in self._universe.CurrentHarborCargo():
            price = 0  # self._priceInterface(cargo)
            yield cargo, price

    def __call__(self, logic):
        print 'Works'
        raw_input()



class StrIntKeys:
    def __init__(self, startIndex=-1):
        self._index = startIndex

    def __call__(self, info):
        self._index += 1
        return str(self._index)
