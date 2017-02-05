import widget as w
import models.models as m


class WidgetHandler:
    def __init__(self, setter, viewer, messages, colors):

        self._buywidget = w.Widget(
            messages=messages.Buy,
            colors=colors,
            interactionfuncs=m.InteractionFuncs(
                linelist=viewer.CargoBuyOptions,
                execute=setter.TradeCargo,
                validator=lambda cargo, price:
                    viewer.FreeCargoSpace() > 0 and viewer.Credits() + price >= 0,
            )
        )

        self._welcomewidget = w.Widget(
            messages=messages.Welcome,
            colors=colors,
            interactionfuncs=m.InteractionFuncs(
                titleargs=lambda: (viewer.HarborName(), ),
            )
        )

        self._statwidget = w.Widget(
            messages=messages.Stats,
            colors=colors,
            interactionfuncs=m.InteractionFuncs(
                titleargs=lambda: (viewer.Credits(), viewer.FreeCargoSpace())
            )
        )

        self._travelwidget = w.Widget(
            messages=messages.Travel,
            colors=colors,
            interactionfuncs=m.InteractionFuncs(
                linelist=viewer.TravelOptions,
                validator=lambda harbor, price: viewer.Credits() - price >= 0,
                execute=setter.Travel,
            )
        )

        self._sellwidget = w.Widget(
            messages=messages.Sell,
            colors=colors,
            interactionfuncs=m.InteractionFuncs(
                linelist=viewer.Cargo,
                validator=lambda cargo, amount, price: True,
                execute=setter.TradeCargo,
            )
        )

    def Travel(self, regfunc):
        return self._travelwidget(regfunc)

    def Buy(self, regfunc):
        return self._buywidget(regfunc)

    def Sell(self, regfunc):
        return self._sellwidget(regfunc)

    def StatsAndInfos(self, regfunc):
        self._welcomewidget(regfunc)
        self._statwidget(regfunc)
