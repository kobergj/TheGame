import universe as u
import player as p

import random

NUMBEROFDESTINATIONS = 3
PRICERANGE = [5, 14]


class LogicViewer:
    def __init__(self, player, universe):
        self._player = p.PlayerViewer(player)
        self._universe = u.UniverseViewer(universe)

    def HarborName(self):
        return self._universe.CurrentHarborName()

    def Credits(self):
        return self._player.GetCredits()

    def Cargo(self):
        return self._player.GetCargo()

    def CargoBuyOptions(self):
        for cargo in self._universe.CurrentHarborCargo():
            yield cargo, self.Price(cargo)

    def TravelOptions(self):
        return self._universe.Destinations(NUMBEROFDESTINATIONS)

    def Price(self, item):
        return random.randint(*PRICERANGE)  # Only Temporary, should be replace by Logic


class StrIntKeys:
    def __init__(self, startIndex=-1):
        self._index = startIndex

    def __call__(self, info):
        self._index += 1
        return str(self._index)
