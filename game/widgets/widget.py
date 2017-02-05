

class Widget:
    def __init__(self, colors, messages, interactionfuncs):
        self._arghandler = RegistryArgumentHandler(
            colors=colors,
            messages=messages,
            interactionfuncs=interactionfuncs,
        )

        self._expandhandler = ExpandHandler(interactionfuncs.linelist is not None)

    def __call__(self, regfunc):
        for args in self._arghandler.IterArguments(self._expandhandler):
            regfunc(*args)


class RegistryArgumentHandler:
    def __init__(self, colors, messages, interactionfuncs):
        self._messages = MessageHandler(messages)
        self._funcs = FuncHandler(interactionfuncs)

        self._colors = ColorHandler(
            deadcol=colors.UnClickable,
            alivecol=colors.Clickable,
            blockedcol=colors.Blocked,
            validator=self._funcs.Validator,
        )

    def Title(self):
        if not self._funcs.Execute:
            col = self._colors.UnClickable
            txt = self._msges.Title(*self._funcs.TitleArgs())
            return col, txt, None

        col = self._colors.Clickable

        if self._funcs.ListFunc and not self._exphdl.IsExpanded():
            txt = self._msges.UnExpanded(*self._funcs.UnExpandedArgs())
        else:
            txt = self._msges.Title(*self._funcs.TitleArgs())

        return col, txt, self._exphdl.Change

    def Lines(self):
        if not self._funcs.ListFunc:
            return

        if not self._exphdl.IsExpanded():
            return

        for args in self._funcs.ListFunc():

            if self._funcs.Validator(*args):
                col = self._colors.Clickable
                txt = self._msges.Line(*self._funcs.LineArgs(*args))
                fnc = self._funcs.Execute
            else:
                col = self._colors.Blocked
                txt = self._msges.Line(*self._funcs.LineArgs(*args))
                fnc = None

            yield col, txt, fnc, args

    def IterArguments(self, expandhandler):
        if not expandhandler.IsExpanded():
            yield self.WidgetLine(
                msg=self._messages.UnExpanded,
                execfunc=expandhandler.Change,
                msgargs=self._funcs.UnExpandedArgs()
            )
            return

        yield self.WidgetLine(
            msg=self._messages.Title,
            execfunc=expandhandler.Change,
            msgargs=self._funcs.TitleArgs(),
        )

        for args in self._funcs.ListFunc():
            yield self.WidgetLine(
                msg=self._messages.Line,
                msgargs=self._funcs.LineArgs(*args),
                execfunc=self._funcs.Execute,
                execargs=args
            )

    def WidgetLine(self, msg, execfunc=None, execargs=[], msgargs=[]):
        return self._colors(execfunc, *execargs), msg(*msgargs), None


class WidgetLine:
    def __init__(self, colors, msg, execfunc):
        self._colors = colors
        self._message = msg
        self._execfunc = execfunc

    def __call__(self, messageargs=[], execargs=[]):
        col = self.Color(*execargs)
        msg = self.Message(*messageargs)
        fun = self.ExecFunc(*execargs)
        return col, msg, fun, execargs

    def Color(self, *execargs):
        return self._colors(self._execfunc, *execargs)

    def Message(self, *msgargs):
        return self._message(*msgargs)

    def ExecFunc(self, *execargs):
        return self._execfunc


class ColorHandler:
    def __init__(self, deadcol, blockedcol, alivecol, validator=lambda *x: True):
        self._deadcol = deadcol
        self._blockedcol = blockedcol
        self._alivecol = alivecol

        self._validator = validator

    def __call__(self, execfunc, *execargs):
        if not execfunc:
            return self._deadcol

        # Will be removed soon
        try:
            if not self._validator(*execargs):
                return self._blockedcol
        except TypeError:
            return self._blockedcol

        return self._alivecol


class FuncHandler:
    def __init__(self, interactionfuncs):
        self.Execute = interactionfuncs.execute
        self.ListFunc = interactionfuncs.linelist

        self.TitleArgs = interactionfuncs.titleargs
        if not self.TitleArgs:
            self.TitleArgs = lambda: ()

        self.LineArgs = interactionfuncs.lineargs
        if not self.LineArgs:
            self.LineArgs = lambda *x: x

        self.Validator = interactionfuncs.validator
        if not self.Validator:
            self.Validator = lambda *x: True

        self.UnExpandedArgs = interactionfuncs.expand
        if not self.UnExpandedArgs:
            self.UnExpandedArgs = self.TitleArgs


class MessageHandler:
    def __init__(self, messages):
        self._messages = messages

    def Title(self, *args):
        return self._messages.Expanded.format(*args)

    def UnExpanded(self, *args):
        return self._messages.UnExpanded.format(*args)

    def Line(self, *args):
        return self._messages.Line.format(*args)


class ExpandHandler:
    def __init__(self, expandable=True):
        self._expanded = True

        if not expandable:
            self.Change = None
            self._expanded = False

    def Change(self):
        self._expanded = not self._expanded

    def IsExpanded(self):
        return self._expanded
