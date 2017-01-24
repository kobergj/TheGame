import setters.logic as c
import getters.logic as vl

import view.view as v


class BetterGame:
    def __init__(self, messages, viewsize, pricerange, destnumber, statnames, colors, margin):
        self._messages = messages
        self._colschemes = colors

        self._view = vl.GameViewer(pricerange, destnumber, statnames)
        self._viz = v.View(viewsize, margin)

        self._showsell = True
        self._showbuy = True

    def NewGame(self, player, universe, fleet):
        self._logic = c.LogicController(player, universe, fleet)
        self._view.NewGame(player, universe, fleet)

    def Recalculate(self):
        # Welcome part
        txt = self._messages.Welcome.format(self._view.HarborName())
        self._viz.RegisterTopMid(self._colschemes.Unclickable, txt, None)

        # Info about Credits
        txt = self._messages.Stats.format(self._view.Credits(), self._view.FreeCargoSpace())
        self._viz.RegisterTopMid(self._colschemes.Unclickable, txt, None)

        # Info about Cargo
        self.AddBuyInfo()
        self.AddSellInfo()

        # Next Harbor
        self.TravelInteraction()
        return self._viz()

    def TravelInteraction(self):
        for harbor in self._view.TravelOptions():
            price = self._view.TravelPrice(harbor)
            info = self._messages.Travel.format(harbor.name, price)

            colscheme = self._colschemes.Clickable
            trfunc = self._logic.Travel
            if self._view.Credits() - price < 0:
                trfunc = None
                colscheme = self._colschemes.Blocked

            self._viz.RegisterBottomMid(colscheme, info, trfunc, harbor, price)

        return

    def AddSellInfo(self):
        def expand():
            self._showsell = not self._showsell

        col = self._colschemes.Clickable

        if not self._showsell:
            self._viz.RegisterBottomLeft(col, self._messages.NoSell, expand)
            return

        self._viz.RegisterBottomLeft(col, self._messages.Sell, expand)
        for cargo, amount, price in self._view.Cargo():
            self._viz.RegisterBottomLeft(
                col,
                self._messages.SellLine.format(cargo, amount, price),
                self._logic.TradeCargo,
                cargo, price
            )

        return

    def AddBuyInfo(self):
        def expand():
            self._showbuy = not self._showbuy

        col, blocked = self._colschemes.Clickable, self._colschemes.Blocked

        if not self._showbuy:
            self._viz.RegisterBottomRight(col, self._messages.NoBuy, expand)
            return

        self._viz.RegisterBottomRight(col, self._messages.Buy, expand)
        for cargo, price in self._view.CargoBuyOptions():

            bfunc = self._logic.TradeCargo
            if self._view.FreeCargoSpace() <= 0:
                bfunc = None
                col = blocked
            if self._view.Credits() - price < 0:
                bfunc = None
                col = blocked

            self._viz.RegisterBottomRight(
                col,
                self._messages.BuyLine.format(cargo, price),
                bfunc,
                cargo, -price
            )

        return
