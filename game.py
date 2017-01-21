import controllers.logic as c
import view.logic as vl

import visualization.view as v
import visualization.fabric as f


WELCOME = " -- Welcome To {} -- "
CREDITS = "[Credits] {}"
CONTINUE = "[ENTER] Continue"

SELLTEMPLATE = "   {}: {} (Sell for {})"
SELL = " [Sell] "
NOSELL = " [SELL] ..."

BUYTEMPLATE = "{} (Buy for {})   "
BUY = "[Buy] "
NOBUY = "... [BUY] "

TRAVELMESSAGE = "[CONTINUE] Next Stop: {}"

FONTNAME = 'arial'
FONTSIZE = 20

WINDOWSIZE = 600, 400
BUTTONSIZE = 600, 30


class Game:
    def __init__(self, player, universe):
        self._logic = c.LogicController(player, universe)
        self._view = vl.LogicViewer(player, universe)
        self._viz = v.View(WINDOWSIZE, BUTTONSIZE, FONTNAME, FONTSIZE, v.BLACK)

        self._showsell = True
        self._showbuy = True

    # @log.Logger("Call Main Loop")
    def __call__(self):
        # Welcome part
        txt = WELCOME.format(self._view.HarborName())
        self._viz.Register(f.TOPMID, txt, None)

        # Info about Credits
        txt = CREDITS.format(self._view.Credits())
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
            info = TRAVELMESSAGE.format(harbor.name)
            self._viz.Register(f.TOPMID, info, self._logic.Travel, harbor)

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
            self._viz.Register(
                f.BOTTOMRIGHT,
                BUYTEMPLATE.format(cargo, price),
                self._logic.TradeCargo,
                cargo, -price
            )

        return


"""
class ButtonRegistryBuilder:
    def __init__(self, wsize, mouse):
        buttonfabric = f.ButtonFabric(wsize, mouse)
        self._reg = r.ExecRegistry(buttonfabric)

    def RegisterClickable(self, msg, func, *args):
        self._reg.Register(
            m.ButtonInfo(
                texts=m.Switch([msg, BLACK], on_highlight=[msg, SOMEELSE]),
                colors=CLICKABLE,
                position=f.TOPLEFT,
                size=BUTTONSIZE,
            ),
            func, *args
        )

    def RegisterUnClickable(self, msg):
        self._reg.Register(
            m.ButtonInfo(
                texts=m.Switch([msg, BLACK], on_highlight=[msg, SOME]),
                colors=UNCLICKABLE,
                position=f.TOPLEFT,
                size=BUTTONSIZE,
            ),
            lambda: None,
        )

    def GetRegistry(self):
        return self._reg
"""
