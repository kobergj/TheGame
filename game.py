import controllers.logic as c
import view.logic as vl
import implementations.registry as r
import implementations.book as b

import visualization.button as but
import visualization.slide as v
import visualization.switch as s


STATSTEMPLATE = """
    -- Welcome To {} --
[Credits] {}  [Cargo] {}
[ENTER] Continue  [q] Quit Game
"""

WELCOME = " -- Welcome To {} -- "
CREDITS = "[Credits] {}"
CARGO = "[Cargo] "
CONTINUE = "[ENTER] Continue"

CARGOTEMPLATE = "{}: {} (Sell for {})"
NOCARGO = "[...]"

BUYMESSAGE = "Buy Cargo '{}' for {} Credits"
SELLMESSAGE = "     Sell Cargo '{}' for {} Credits"
TRAVELMESSAGE = "Travel to '{}'"

WINDOWSIZE = 600, 400
BUTTONSIZE = 600, 50

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
SOME, SOMEELSE = (123, 12, 178), (30, 200, 96)

CLICKABLE = s.Switch(
    on_passive=(WHITE, BLACK),
    on_active=(WHITE, BLACK),
    on_highlight=(SOME, SOMEELSE),
    on_click=(SOMEELSE, SOME)
)

UNCLICKABLE = s.Switch(
    on_passive=(WHITE, BLACK),
    on_active=(WHITE, BLACK),
    on_highlight=(WHITE, BLACK),
    on_click=(WHITE, BLACK)
)


class Game:
    def __init__(self, player, universe):
        self._logic = c.LogicController(player, universe)
        self._view = vl.LogicViewer(player, universe)
        self._viz = v.View(WINDOWSIZE, BUTTONSIZE)

        self._gamebook = b.Book(self.TravelInteraction, self.BuyInteraction)

        self._showcargo = False

    # @log.Logger("Call Main Loop")
    def __call__(self):
        self._viz.Handle()

        reg = ButtonRegistry(WINDOWSIZE, BUTTONSIZE)

        # Welcome part
        txt = WELCOME.format(self._view.HarborName())
        reg.RegisterUnClickable(txt, lambda: None)

        # Info about Credits
        txt = CREDITS.format(self._view.Credits())
        reg.RegisterUnClickable(txt, lambda: None)

        # Info about Cargo
        reg = self.CargoInfo(reg)

        # Next Slide
        reg.RegisterClickable(CONTINUE, self._gamebook.TurnPage)

        # Options
        reg = self._gamebook.Read()(reg)

        # Visualize
        self._viz(reg.GetRegistry())

    def TravelInteraction(self, reg):
        for harbor in self._view.TravelOptions():
            info = TRAVELMESSAGE.format(harbor.name)
            reg.RegisterClickable(info, self._logic.Travel, harbor)

        return reg

    def BuyInteraction(self, reg):
        for cargo, price in self._view.CargoBuyOptions():
            info = BUYMESSAGE.format(cargo, price)
            reg.RegisterClickable(info, self._logic.TradeCargo, cargo, -price)

        return reg

    def CargoInfo(self, reg):
        def expand():
            self._showcargo = not self._showcargo

        if not self._showcargo:
            reg.RegisterClickable(NOCARGO, expand)
            return reg

        reg.RegisterClickable(CARGO, expand)
        for cargo, amount in self._view.Cargo():
            price = self._view.Price(cargo)
            reg.RegisterClickable(
                CARGOTEMPLATE.format(cargo, amount, price),
                self._logic.TradeCargo,
                cargo, price
            )

        return reg


class ButtonRegistry:
    def __init__(self, wsize, bsize):
        buttonfabric = but.ButtonKeys(wsize, bsize)
        self._reg = r.ExecRegistry(buttonfabric)

    def RegisterClickable(self, msg, func, *args):
        self._reg.Register(
            but.Info(
                msg,
                CLICKABLE,
            ),
            func, *args
        )

    def RegisterUnClickable(self, msg, func, *args):
        self._reg.Register(
            but.Info(
                msg,
                UNCLICKABLE,
            ),
            func, *args
        )

    def GetRegistry(self):
        return self._reg
