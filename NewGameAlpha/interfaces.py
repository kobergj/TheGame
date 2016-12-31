import actions as act
import container as gs
import factory as fac

import models as m
import logger as log

CREDITCURRENCYNAME = "Credits"

BUYMESSAGE = "Buy Cargo '%s'"
TRAVELMESSAGE = "Travel to '%s'"
QUITMESSAGE = "Quit Game"


class PlayerInterface:
    def __init__(self, playername):
        self._player = m.Player(
            name=playername,
            cargoInterface=CargoInterface(),
            creditsInterface=CreditInterface(),
            choiceInterface=ChoiceInterface(),
        )

        self._harborfactory = fac.SampleHarborFactory()

        self._harbor = self._harborfactory.RandomHarbor()

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
        return self._player.choiceInterface(self)

    def CurrentHarbor(self):
        return self._harbor

    def NextHarbor(self):
        return self._harborfactory.RandomHarbor()


class CargoInterface:
    def __init__(self):
        self._cargo = gs.Container()

    @log.Logger('Call Cargo Interface')
    def __call__(self, cargo=None):
        if not cargo:
            return self._cargo

        return self._cargo + cargo


class CreditInterface:
    def __init__(self, startCredits=0):
        self._credits = gs.Container()

    @log.Logger('Call Credit Interface')
    def __call__(self, amount=1):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._credits.manipulate(c, amount)[1]


class ChoiceInterface:
    def __init__(self):
        self._choices = None

    @log.Logger('Call Choices Interface')
    def __call__(self, player):
        harbor = player.CurrentHarbor()
        actions = list()

        # Items
        for cargo in harbor.cargo:
            action = act.BuyItem(BUYMESSAGE % str(cargo), cargo)

            if action.available(player):
                actions.append(action)

        # Travel
        dest = player.NextHarbor()
        actions.append(act.Travel(TRAVELMESSAGE % str(dest), m.Space(dest)))

        # Quit
        actions.append(act.Quit(QUITMESSAGE, None))

        return actions
