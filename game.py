import controllers.logic as c
import view.logic as vl
import view.view as v
import implementations.registry as r
import implementations.book as b
import helpers.logger as log


STATSTEMPLATE = """
    -- Welcome To {} --
[Credits] {}  [Cargo] {}
[ENTER] Continue  [q] Quit Game
"""

CARGOTEMPLATE = "{}x{}"

BUYMESSAGE = "[{}] Buy Cargo '{}' for {} Credits"
SELLMESSAGE = "[{}] Sell Cargo '{}' for {} Credits"
TRAVELMESSAGE = "[{}] Travel to '{}'"


class Game:
    def __init__(self, player, universe):
        self._logic = c.LogicController(player, universe)
        self._view = vl.LogicViewer(player, universe)
        self._viz = v.View()

        self._gamebook = b.Book(self.TravelInteraction, self.SellInteraction, self.BuyInteraction)

    def __nonzero__(self):
        return self._viz._alive

    @log.Logger("Call Main Loop")
    def __call__(self):
        reg = r.ExecRegistry(vl.StrIntKeys())

        statinfo = v.Info(
            STATSTEMPLATE,
            self._view.HarborName(),
            self._view.Credits(),
            [CARGOTEMPLATE.format(str(c), a) for c, a in self._view.Cargo()],
        )
        reg.Register(statinfo, self._gamebook.TurnPage)

        reg = self._gamebook.Read()(reg)

        self._viz(reg)

    def TravelInteraction(self, reg):
        for harbor in self._view.TravelOptions():
            reg.Register(v.Info(TRAVELMESSAGE, harbor.name), self._logic.Travel, harbor)

        return reg

    def BuyInteraction(self, reg):
        for cargo, price in self._view.CargoBuyOptions():
            reg.Register(v.Info(BUYMESSAGE, cargo, price), self._logic.TradeCargo, cargo, -price)

        return reg

    def SellInteraction(self, reg):
        for cargo, _ in self._view.Cargo():
            price = self._view.Price(cargo)
            reg.Register(v.Info(SELLMESSAGE, cargo, price), self._logic.TradeCargo, cargo, price)

        return reg
