import universe as u
import player as p
import fleet as f

import random


class GameViewer:
    def __init__(self, pricerange, destnumber, statnames):
        self._priceregistry = PriceRegistry(pricerange)
        self._numberofdest = destnumber
        self._statnames = statnames

    def NewGame(self, player, universe, fleet):
        self._player = p.PlayerViewer(player)
        self._universe = u.UniverseViewer(universe)
        self._fleet = f.FleetViewer(fleet)

    def HarborName(self):
        return self._universe.CurrentHarborName()

    def Credits(self):
        return self._player.GetCredits()

    def Cargo(self):
        for cargo, amount in self._player.GetCargo():
            yield cargo, amount, self.Price(cargo)

    def CargoBuyOptions(self):
        for cargo in self._universe.CurrentHarborCargo():
            yield cargo, self.Price(cargo)

    def TravelOptions(self):
        return self._universe.Destinations(self._numberofdest)

    def Price(self, item):
        return self._priceregistry.Get(self._universe.CurrentHarborName(), item)

    def TravelPrice(self, harbor):
        return self._fleet.GetStat(self._statnames.TravelCosts)

    def FreeCargoSpace(self):
        used = self._player.UsedCargoSpace()
        cap = self._fleet.GetStat(self._statnames.CargoCapacity)
        return cap - used


class PriceRegistry:
    def __init__(self, pricerange):
        self._prices = {}
        self._pricerange = pricerange

    def Get(self, harbor, cargo):
        if harbor not in self._prices:
            self._prices[harbor] = {}

        if cargo not in self._prices[harbor]:
            self._prices[harbor][cargo] = random.randint(*self._pricerange)

        return self._prices[harbor][cargo]
