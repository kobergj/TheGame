import player as p
import universe as u

import models as m

PLAYERNAME = "Players Name"

BUYMESSAGE = "Buy Cargo '%s' for %s"
TRAVELMESSAGE = "Travel to '%s'"
QUITMESSAGE = "Quit Game"

UNIVERSENAME = ["Pegasus"]
SAMPLECARGO = ["Sample Cargo", "Another Cargo"]
SAMPLEHARBORS = ["Safe Harbor", "Even safer Harbor"]


class LogicController:
    def __init__(self):
        player = m.Player(PLAYERNAME)
        self._playerInterface = p.PlayerController(player)

        universe = m.Universe(UNIVERSENAME, SAMPLEHARBORS, SAMPLECARGO)
        self._universeInterface = u.UniverseController(universe)

        self._priceInterface = u.PriceController()

    def CargoBuyOptions(self):
        harbor = u.HarborController(self._universeInterface.GetHarbor())

        options = list()
        for cargo in harbor.IterateCargo():
            price = self._priceInterface(cargo)
            options.append((cargo, price))

        def buy(i):
            cargo, price = options[i]
            self.TradeCargo(cargo, -price)

        return m.Action(BUYMESSAGE, options, buy)

    def TradeCargo(self, cargo, credits):
        self._player.Credits(credits)
        self._player.AddCargo(cargo)

    def Travel(self, harbor):
        self._universeInterface.SwitchHarbor(harbor)
