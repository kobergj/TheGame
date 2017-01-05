import actions as act
import container as gs
import factory as fac

import models as m
import logger as log

CREDITCURRENCYNAME = "Credits"

BUYMESSAGE = "Buy Cargo '%s'"
TRAVELMESSAGE = "Travel to '%s'"
QUITMESSAGE = "Quit Game"


class LogicInterface:
    def __init__(self, playername):
        player = m.Player(name=playername)
        self._playerInterface = PlayerInterface(player)

        space = m.Space()
        self._spaceInterface = SpaceInterface(space)

        self._priceInterface = PriceInterface()


class PlayerInterface:
    def __init__(self, player):
        self._player = player

        self._cargoInterface = CargoInterface()
        self._creditsInterface = CreditInterface()

        self.ingamingmood = True

    def __call__(self, action):
        action(self)

    def __nonzero__(self):
        return self.ingamingmood

    def Credits(self, amount=0):
        return self._creditsInterface(amount)

    def Cargo(self, cargo=None):
        return self._cargoInterface(cargo)


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


class SpaceInterface:
    def __init__(self, space):
        self._space = space
        self._harborfactory = fac.SampleHarborFactory()

        self.SwitchHarbor(self.NewHarbor())

    def SwitchHarbor(self, harbor):
        self._currentHarbor = harbor

    def GetHarbor(self):
        return self._currentHarbor

    def NewHarbor(self):
        return HarborInterface(self._harborfactory.RandomHarbor())


class HarborInterface:
    def __init__(self, harbor):
        self._harbor = harbor

    def IterateCargo(self):
        for cargo in self._harbor.cargo:
            yield cargo

    def GetPrice(self, cargo):
        return self._harbor.pricefactory(cargo)


class PriceInterface:
    def __init__(self):
        self._priceFactory = fac.PriceFactory()

    def __call__(self, item):
        return self._priceFactory(item)
