import player as p
import universe as u
import helpers.logger as log


class LogicController:
    def __init__(self, player, universe):
        self._player = p.PlayerController(player)

        self._universe = u.UniverseController(universe)

    def TradeCargo(self, cargo, credits):
        self._player.Trade(credits, cargo)

    @log.Logger("Call Logic Controller")
    def Travel(self, harbor, price):
        success = self._player.Trade(-price)
        if success:
            self._universe.Travel(harbor)
