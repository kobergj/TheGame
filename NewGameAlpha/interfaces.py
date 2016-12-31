import actions as act
import container as gs

import models as m

CREDITCURRENCYNAME = "Credits"
STARTHARBORNAME = "Safe Harbor"

SAMPLECARGO = "Sample Cargo"
SAMPLEPRICE = 12


class PlayerInterface:
    def __init__(self, playername):
        self._player = m.Player(
            name=playername,
            cargoInterface=CargoInterface(),
            creditsInterface=CreditInterface(),
            choiceInterface=ChoiceInterface(),
        )

        self._harbor = m.Harbor(STARTHARBORNAME)

        self.ingamingmood = True

    def __call__(self, action):
        action(self)

    def __nonzero__(self):
        return self.ingamingmood

    def Credits(self, amount=0):
        return self._player.creditsInterface(amount)

    def Cargo(self, cargo=None):
        return self._player.cargoInterface(cargo)

    def Choices(self):
        harbor = self._harbor

        return self._player.choiceInterface(harbor)

    def CurrentHarbor(self):
        return self._harbor


class CargoInterface:
    def __init__(self):
        self._cargo = gs.Container()

    def __call__(self, cargo=None):
        if not cargo:
            return self._cargo

        return self._cargo + cargo


class CreditInterface:
    def __init__(self, startCredits=0):
        self._credits = gs.Container()

    def __call__(self, amount=1):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._credits.manipulate(c, amount)[1]


class ChoiceInterface:
    def __init__(self):
        self._choices = None

    def __call__(self, harbor):
        return [
            act.BuyItem('Buy Item %s' % SAMPLECARGO, m.Cargo(SAMPLECARGO, SAMPLEPRICE)),
            act.Quit('Quit Game', None)
        ]
