import player as p
import universe as u

import models.models as m

PLAYERNAME = "Players Name"

BUYMESSAGE = "Buy Cargo '%s' for %s"
TRAVELMESSAGE = "Travel to '%s'"
QUITMESSAGE = "Quit Game"

UNIVERSENAME = ["Pegasus"]
SAMPLECARGO = [[m.Cargo("Sample Cargo"), 1], [m.Cargo("Another Cargo"), 1]]
SAMPLEHARBORS = [[m.Harbor("Safe Harbor"), 1], [m.Harbor("Even safer Harbor"), 0]]

STARTCURRENCY = [m.Currency("Credits"), 12]


class LogicController:
    def __init__(self, player, universe):
        self._playerInterface = p.PlayerController(player)

        self._universeController = u.UniverseController(universe)

        self._priceInterface = u.PriceController()

    def TradeCargo(self, cargo, credits):
        self._player.Credits(credits)
        self._player.AddCargo(cargo)

    def Travel(self, harbor):
        self._universeInterface.Travel(harbor)
