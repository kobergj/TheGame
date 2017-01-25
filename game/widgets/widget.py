

class WidgetHandler:
    def __init__(self, setter, viewer, messages, colors):

        self._buywidget = Widget(
            messages=messages.Buy,
            colors=colors,
            validator=lambda cargo, price:
                viewer.FreeCargoSpace() > 0 and viewer.Credits() + price >= 0,
            execfunc=setter.TradeCargo,
            optionfunc=viewer.CargoBuyOptions,
        )

        self._welcomewidget = Widget(
            messages=messages.Welcome,
            colors=colors,
            optionfunc=lambda: (viewer.HarborName(), ),
            expendable=False,
        )

        self._statwidget = Widget(
            messages=messages.Stats,
            colors=colors,
            optionfunc=lambda: (viewer.Credits(), viewer.FreeCargoSpace()),
            expendable=False,
        )

        self._travelwidget = Widget(
            messages=messages.Travel,
            colors=colors,
            optionfunc=viewer.TravelOptions,
            validator=lambda harbor, price: viewer.Credits() - price >= 0,
            execfunc=setter.Travel,
            expendable=False,
        )

        self._sellwidget = Widget(
            messages=messages.Sell,
            colors=colors,
            optionfunc=viewer.Cargo,
            validator=lambda cargo, amount, price: True,
            execfunc=setter.TradeCargo,
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


class Widget:
    def __init__(self, messages, colors, optionfunc, validator=None, execfunc=None, expendable=True):
        self._messages = messages
        self._colors = colors
        self._validator = validator
        self._execfunc = execfunc
        self._optionfunc = optionfunc

        self._show = True
        self._expendable = expendable

    def Expand(self):
        self._show = not self._show

    def __call__(self, regfunc):
        args = list(self._optionfunc())

        if not self._execfunc:
            regfunc(self._colors.UnClickable, self._messages.Expanded.format(*args), None)
            return

        col = self._colors.Clickable
        if not self._show and self._expendable:
            regfunc(col, self._messages.UnExpanded.format(*args), self.Expand)
            return

        regfunc(col, self._messages.Expanded.format(*args), self.Expand)
        for innerargs in args:
            if self._validator(*innerargs):
                regfunc(col, self._messages.Line.format(*innerargs), self._execfunc, *innerargs)
                continue

            regfunc(self._colors.Blocked, self._messages.Line.format(*innerargs), None)
