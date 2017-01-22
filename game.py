import controllers.logic as c
import view.logic as vl

import visualization.view as v
import visualization.fabric as f


import helpers.kindaconfiguration as conf
# Configuration Access
WELCOME = conf.Messages.Welcome
STATS = conf.Messages.Stats
SELLTEMPLATE = conf.Messages.SellLine
SELL = conf.Messages.Sell
NOSELL = conf.Messages.NoSell
BUYTEMPLATE = conf.Messages.BuyLine
BUY = conf.Messages.Buy
NOBUY = conf.Messages.NoBuy
TRAVELMESSAGE = conf.Messages.Travel
FONTNAME = conf.Layout.Font
FONTSIZE = conf.Layout.FontSize
WINDOWSIZE = conf.Layout.WindowSize
# Configuration Access End


class Game:
    def __init__(self, player, universe):
        self._logic = c.LogicController(player, universe)
        self._view = vl.LogicViewer(player, universe)
        self._viz = v.View(WINDOWSIZE, FONTNAME, FONTSIZE, v.BLACK)

        self._showsell = True
        self._showbuy = True

    # @log.Logger("Call Main Loop")
    def __call__(self):
        # Welcome part
        txt = WELCOME.format(self._view.HarborName())
        self._viz.Register(f.TOPMID, txt, None)

        # Info about Credits
        txt = STATS.format(self._view.Credits(), self._view.FreeCargoSpace())
        self._viz.Register(f.TOPMID, txt, None)

        # Info about Cargo
        self.AddBuyInfo()
        self.AddSellInfo()

        # Next Harbor
        self.TravelInteraction()

        # Visualize
        self._viz()

    def TravelInteraction(self):
        for harbor in self._view.TravelOptions():
            price = self._view.TravelPrice(harbor)
            info = TRAVELMESSAGE.format(harbor.name, price)

            trfunc = self._logic.Travel
            if self._view.Credits() - price < 0:
                trfunc = None

            self._viz.Register(f.TOPMID, info, trfunc, harbor, price)

        return

    def AddSellInfo(self):
        def expand():
            self._showsell = not self._showsell

        if not self._showsell:
            self._viz.Register(f.BOTTOMLEFT, NOSELL, expand)
            return

        self._viz.Register(f.BOTTOMLEFT, SELL, expand)
        for cargo, amount, price in self._view.Cargo():
            self._viz.Register(
                f.BOTTOMLEFT,
                SELLTEMPLATE.format(cargo, amount, price),
                self._logic.TradeCargo,
                cargo, price
            )

        return

    def AddBuyInfo(self):
        def expand():
            self._showbuy = not self._showbuy

        if not self._showbuy:
            self._viz.Register(f.BOTTOMRIGHT, NOBUY, expand)
            return

        self._viz.Register(f.BOTTOMRIGHT, BUY, expand)
        for cargo, price in self._view.CargoBuyOptions():

            bfunc = self._logic.TradeCargo
            if self._view.FreeCargoSpace() <= 0:
                bfunc = None
            if self._view.Credits() - price < 0:
                bfunc = None

            self._viz.Register(
                f.BOTTOMRIGHT,
                BUYTEMPLATE.format(cargo, price),
                bfunc,
                cargo, -price
            )

        return
