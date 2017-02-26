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
        return Interaction(it.Buy, self._setter.TradeCargo, self._viewer.CargoBuyOptions)


class Interaction:
    def __init__(self, typ, execfunc, argsfunc):
        self._execfunc = execfunc
        self._argsfunc = argsfunc
        self._type = typ

    def Func(self):
        return self._execfunc

    def Args(self):
        for args in self._argsfunc():
            yield args

    def Type(self):
        return self._type
