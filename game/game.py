import setters.logic as c
import getters.logic as vl

from models.constants import InteractionTypes as it


class GameModel:
    def __init__(self, pricerange, destnumber, statnames):
        self._viewer = vl.GameViewer(pricerange, destnumber, statnames)

    def NewGame(self, player, universe, fleet):
        self._setter = c.GameSetter(player, universe, fleet)
        self._viewer.NewGame(player, universe, fleet)

    def Buy(self):
        return Interaction(
            typ=it.Buy,
            execfunc=self._setter.TradeCargo,
            argsfunc=self._viewer.CargoBuyOptions,
            valfunc=lambda cargo, price:
                self._viewer.FreeCargoSpace() > 0 and self._viewer.Credits() + price >= 0,
        )

    def Sell(self):
        return Interaction(it.Sell, self._setter.TradeCargo, self._viewer.Cargo)

    def Stats(self):
        return Interaction(it.Stats, lambda *x: None, self._viewer.Stats)

    def Travel(self):
        return Interaction(it.Travel, self._setter.Travel, self._viewer.TravelOptions)

    def Harbor(self):
        return Interaction(it.Info, lambda *x: None, self._viewer.Harbor)


class Interaction:
    def __init__(self, typ, execfunc, argsfunc, valfunc=lambda *x: True):
        self._execfunc = execfunc
        self._argsfunc = argsfunc
        self._type = typ
        self._validator = valfunc

    def Func(self):
        return self._execfunc

    def Args(self):
        for args in self._argsfunc():
            yield args

    def Type(self):
        return self._type

    def Validator(self):
        return self._validator
