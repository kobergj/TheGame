import controllers.logic as c
import view.logic as vl
import view.view as v
import implementations.registry as r

class Game:
    def __init__(self, player, universe):
        self._logic = c.LogicController(player, universe)
        self._view = vl.LogicViewer(player, universe)

    def __nonzero__(self):
        viz = v.View()
        buyreg = self.BuyInteraction()
        viz.BuyOptions(buyreg)

        return self._view

    def BuyInteraction(self):
        reg = r.ExecRegistry(vl.StrIntKeys())

        for cargo, price in self._view.CargoBuyOptions():
            reg.Register(None, self._logic.TradeCargo, cargo, price)

        return reg


