
class Fleet:
    def __init__(self, fleet):
        self._fleet = fleet

        for ship in self._fleet.standbyships:
            self.AttachShip(ship)

    def AddShip(self, ship):
        self._fleet.standbyships + ship

    def AttachShip(self, ship):
        self._fleet.stats += ship.stats
        self._fleet.activeships + ship
        self._fleet.standbyships - ship

    def DetachShip(self, ship):
        self._fleet.stats -= ship.stats
        self._fleet.activeships - ship
        self._fleet.standbyships + ship
