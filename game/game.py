import setters.logic as c
import getters.logic as vl

import view.view as v
import view.fabric as f


class BetterGame:
    def __init__(self, messages, viewsize, mouse, pricerange, destnumber, statnames):
        self._view = vl.GameViewer(pricerange, destnumber, statnames)
        self._viz = v.View(viewsize, mouse)
        self._messages = messages

        self._showsell = True
        self._showbuy = True

    def __call__(self, vizapi):
        self.Recalculate()
        self.Visualize(vizapi)

    def NewGame(self, player, universe, fleet):
        self._logic = c.LogicController(player, universe, fleet)
        self._view.NewGame(player, universe, fleet)

    def Recalculate(self):
        # Welcome part
        txt = self._messages.Welcome.format(self._view.HarborName())
        self._viz.Register(f.TOPMID, txt, None)

        # Info about Credits
        txt = self._messages.Stats.format(self._view.Credits(), self._view.FreeCargoSpace())
        self._viz.Register(f.TOPMID, txt, None)

        # Info about Cargo
        self.AddBuyInfo()
        self.AddSellInfo()

        # Next Harbor
        self.TravelInteraction()

    def TravelInteraction(self):
        for harbor in self._view.TravelOptions():
            price = self._view.TravelPrice(harbor)
            info = self._messages.Travel.format(harbor.name, price)

            trfunc = self._logic.Travel
            if self._view.Credits() - price < 0:
                trfunc = None

            self._viz.Register(f.TOPMID, info, trfunc, harbor, price)

        return

    def AddSellInfo(self):
        def expand():
            self._showsell = not self._showsell

        if not self._showsell:
            self._viz.Register(f.BOTTOMLEFT, self._messages.NoSell, expand)
            return

        self._viz.Register(f.BOTTOMLEFT, self._messages.Sell, expand)
        for cargo, amount, price in self._view.Cargo():
            self._viz.Register(
                f.BOTTOMLEFT,
                self._messages.SellLine.format(cargo, amount, price),
                self._logic.TradeCargo,
                cargo, price
            )

        return

    def AddBuyInfo(self):
        def expand():
            self._showbuy = not self._showbuy

        if not self._showbuy:
            self._viz.Register(f.BOTTOMRIGHT, self._messages.NoBuy, expand)
            return

        self._viz.Register(f.BOTTOMRIGHT, self._messages.Buy, expand)
        for cargo, price in self._view.CargoBuyOptions():

            bfunc = self._logic.TradeCargo
            if self._view.FreeCargoSpace() <= 0:
                bfunc = None
            if self._view.Credits() - price < 0:
                bfunc = None

            self._viz.Register(
                f.BOTTOMRIGHT,
                self._messages.BuyLine.format(cargo, price),
                bfunc,
                cargo, -price
            )

        return

    def Visualize(self, vizapi):
        # Visualize
        self._viz(vizapi)
