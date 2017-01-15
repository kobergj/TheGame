import helpers.logger as log


STATSTEMPLATE = """
    -- Welcome To %s --
[Credits] %s  [Cargo] %s
[ENTER] Continue  [q] Quit Game
"""

BUYMESSAGE = "[%s] Buy Cargo '%s' for %s Credits"
TRAVELMESSAGE = "[%s] Travel to '%s'"


class View:
    def __init__(self):
        self._alive = True

    def __nonzero__(self):
        return self._alive

    @log.Logger("Call Visualizing")
    def __call__(self, reg):
        con = Controller(reg)

        s = Stringer(reg["0"].Unpack())
        for key, _ in reg:
            if key != "0":
                s.AddLine(reg[key].Unpack(key))

        c, self._alive = con(str(s))

        return reg(c)


class Info:
    def __init__(self, template, *args):
        self._template = template
        self._args = args

    def Unpack(self, key=None):
        allargs = []
        if key:
            allargs.append(key)
        allargs.extend(a for a in self._args)
        return self._template.format(*allargs)


class Stringer:
    def __init__(self, start):
        self._string = start

    def __str__(self):
        return self._string

    def AddLine(self, string):
        self._string += "\n"
        self._string += string


class Controller:
    def __init__(self, reg):
        self._validator = Validator(reg)

    @log.Logger("Call Terminal Controller")
    def __call__(self, info):
        print info

        c = None
        while not self._validator(c):
            c = raw_input()

            if c == "q":
                return None, False

            if c == "":
                return "0", True

        return c, True


class Validator:
    def __init__(self, accepted):
        self._accepted = accepted

    def __call__(self, candidate):
        if candidate in self._accepted:
            return True

        return False
