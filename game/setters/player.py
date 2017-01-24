import helpers.logger as log
import models.models as m


class PlayerController:
    def __init__(self, player):
        self._player = player

        self._cargoController = CargoController(player.cargo)
        self._currencyController = CurrencyController(player.currency)

    def Trade(self, credits=0, cargo=None):
        self._currencyController.TradeCredits(credits)

        if cargo:
            if credits < 0:
                self._cargoController.AddCargo(cargo)

            if credits > 0:
                self._cargoController.RemoveCargo(cargo)

        return True


class CargoController:
    def __init__(self, startCargo):
        self._cargo = startCargo

    @log.Logger('Call Cargo Controller')
    def GetCargoAmount(self, item):
        return self._cargo[item]

    def AddCargo(self, cargo):
        self._cargo + cargo

    def RemoveCargo(self, cargo):
        self._cargo - cargo


class CurrencyController:
    def __init__(self, startCredits):
        self._credits = startCredits

    @log.Logger('Call Credit Controller')
    def GetCredits(self):
        return self._credits[m.Credits()]

    def TradeCredits(self, amount):
        self._credits.manipulate(m.Credits(), amount)
