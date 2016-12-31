import actions as act
import gamestats as gs

import models as m

CREDITCURRENCYNAME = "Credits"


class Player:
    def __init__(self, name, startharbor):
        self.name = name

        self._harbor = startharbor

        self._ingamingmood = True

        # Player Stats
        self._credits = gs.Container()
        self._cargo = gs.Container()

    def __call__(self, action):
        if str(action) == 'Fly Away':
            self._ingamingmood = False

        action(self)

    def __nonzero__(self):
        return self._ingamingmood

    def Credits(self, amount=0):
        c = m.Currency(CREDITCURRENCYNAME)
        return self._credits.manipulate(c, amount)[1]

    def Cargo(self, cargo=None):
        if not cargo:
            return self._cargo

        return self._cargo + cargo

    def Choices(self):
        harbor = self._harbor

        return [
            act.Action('Buy Item', harbor),
            act.Action('Sell Item', harbor),
            act.Action('Fly Away', harbor),
        ]

    def CurrentHarbor(self):
        return self._harbor
