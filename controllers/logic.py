import player as p
import universe as u
import fleet as f

import helpers.logger as log


class LogicController:
    def __init__(self, player, universe, fleet):
        self._player = p.PlayerController(player)
        self._universe = u.UniverseController(universe)
        self._fleet = f.Fleet(fleet)

    def TradeCargo(self, cargo, credits):
        self._player.Trade(credits, cargo)

    @log.Logger("Call Logic Controller")
    def Travel(self, harbor, price):
        success = self._player.Trade(-price)
        if success:
            self._universe.Travel(harbor)

    def ManipulateFleet(self, activate=None, deactivate=None, add=None):
        if add:
            self._fleet.AddShip(add)

        if deactivate:
            self._fleet.DetachShip(deactivate)

        if activate:
            self._fleet.AttachShip(activate)
