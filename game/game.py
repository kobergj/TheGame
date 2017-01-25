import setters.logic as c
import getters.logic as vl
import widgets.widget as w
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

        self._widgets = w.WidgetHandler(
            setter=self._logic,
            viewer=self._view,
            messages=self._messages,
            colors=self._colschemes
        )

    def Recalculate(self):
        self._widgets.StatsAndInfos(self._viz.RegisterTopMid)
        self._widgets.Buy(self._viz.RegisterBottomRight)
        self._widgets.Travel(self._viz.RegisterTopMid)
        self._widgets.Sell(self._viz.RegisterBottomLeft)
        return self._viz()

