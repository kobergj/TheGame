import player as p
import universe as u

PLAYERNAME = "Players Name"

BUYMESSAGE = "Buy Cargo '%s' for %s"
TRAVELMESSAGE = "Travel to '%s'"
QUITMESSAGE = "Quit Game"


class LogicController:
    def __init__(self, player, universe):
        self._player = p.PlayerController(player)

        self._universe = u.UniverseController(universe)

        self._priceInterface = u.PriceController()

    def TradeCargo(self, cargo, credits):
        self._player.Trade(credits, cargo)

    def Travel(self, harbor):
        self._universe.Travel(harbor)
