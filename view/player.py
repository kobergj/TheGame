import models.models as m

CREDITCURRENCYNAME = "Credits"


class PlayerViewer:
    def __init__(self, player):
        self._player = player

        self._cargoViewer = CargoViewer(player.cargo)
        self._currencyViewer = CurrencyViewer(player.currency)

    def Name(self):
        return self._player.name

    def GetCargo(self):
        return self._cargoViewer.GetAll()

    def GetCargoAmount(self, cargo):
        return self._cargoViewer.GetCargoAmount(cargo)

    def GetCredits(self):
        return self._currencyViewer.GetCreditAmount()


class CargoViewer:
    def __init__(self, cargo):
        self._cargo = cargo

    def GetAll(self):
        cargo = list()
        for c, _ in self._cargo:
            cargo.append(c)

        return cargo

    def GetCargoAmount(self, key):
        return self._cargo[key][1]


class CurrencyViewer:
    def __init__(self, currency):
        self._currency = currency

    def GetCreditAmount(self):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._currency[c]
