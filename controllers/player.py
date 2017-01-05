import helpers.logger as log
import implementations.container as gs
import models.models as m

CREDITCURRENCYNAME = "Credits"


class PlayerController:
    def __init__(self, player):
        self._player = player

        self._cargoController = CargoController()
        self._currencyController = CurrencyController()

    def Trade(self, credits=0, cargo=None):
        self._currencyController.TradeCredits(credits)

        if cargo:
            if credits < 0:
                self._cargoController.AddCargo(cargo)

            if credits > 0:
                self._cargoController.RemoveCargo(cargo)


class CargoController:
    def __init__(self):
        self._cargo = gs.Container()

    @log.Logger('Call Cargo Controller')
    def GetCargoAmount(self, item):
        return self._cargo[item][1]

    def AddCargo(self, cargo):
        self._cargo + cargo

    def RemoveCargo(self, cargo):
        self._cargo - cargo


class CurrencyController:
    def __init__(self):
        self._credits = gs.Container()

    @log.Logger('Call Credit Controller')
    def GetCredits(self):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._credits[c][1]

    def TradeCredits(self, amount):
        c = m.Currency(CREDITCURRENCYNAME)
        self._credits.manipulate(c, amount)
