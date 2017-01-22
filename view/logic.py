import universe as u
import player as p
import fleet as f

import random

import helpers.kindaconfiguration as conf
# Configuration Access
NUMBEROFDESTINATIONS = conf.Limits.NumberOfDestinations
PRICERANGE = conf.Limits.PriceRange
TRAVELPRICE = conf.Limits.TravelPrice
CARGOCAP = conf.Stats.CargoCapacity
TRAVELCOST = conf.Stats.TravelCosts
# Configuration Access End


class LogicViewer:
    def __init__(self, player, universe, fleet):
        self._player = p.PlayerViewer(player)
        self._universe = u.UniverseViewer(universe)
        self._fleet = f.FleetViewer(fleet)
        self._priceregistry = PriceRegistry(PRICERANGE)

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
        return self._universe.Destinations(NUMBEROFDESTINATIONS)

    def Price(self, item):
        return self._priceregistry.Get(self._universe.CurrentHarborName(), item)

    def TravelPrice(self, harbor):
        return self._fleet.GetStat(TRAVELCOST)

    def FreeCargoSpace(self):
        used = self._player.UsedCargoSpace()
        cap = self._fleet.GetStat(CARGOCAP)
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
