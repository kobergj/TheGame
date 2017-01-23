import models.models as m

import helpers.kindaconfiguration as conf
# Configuration Access
CREDITCURRENCYNAME = conf.Currencies.Credits
# Configuration Access End


class PlayerViewer:
    def __init__(self, player):
        self._player = player

        self._cargoViewer = CargoViewer(player.cargo)
        self._currencyViewer = CurrencyViewer(player.currency)

    def Name(self):
        return self._player.name

    def GetCargo(self):
        for cargo in self._cargoViewer.GetAll():
            yield cargo, self.GetCargoAmount(cargo)

    def GetCargoAmount(self, cargo):
        return self._cargoViewer.GetCargoAmount(cargo)

    def GetCredits(self):
        return self._currencyViewer.GetCreditAmount()

    def UsedCargoSpace(self):
        used = 0
        for _, amount in self.GetCargo():
            used += amount
        return used


class CargoViewer:
    def __init__(self, cargo):
        self._cargo = cargo

    def GetAll(self):
        cargo = list()
        for c in self._cargo:
            cargo.append(c)

        return cargo

    def GetCargoAmount(self, key):
        return self._cargo[key]


class CurrencyViewer:
    def __init__(self, currency):
        self._currency = currency

    def GetCreditAmount(self):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._currency[c]
