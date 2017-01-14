import strviz as s

CONTINUE = "[ENTER] Continue"
BUYMESSAGE = "[%s] Buy Cargo '%s'"
QUIT = "[q] Quit Game"


class View:
    def __init__(self):
        self._alive = True

        def extractBuyInfo(info):
            return info[0], info[1]
        self._buystringer = s.RegistryStringer(extractBuyInfo, BUYMESSAGE)

    def __nonzero__(self):
        return self._alive

    def BuyOptions(self, buyreg):

        controller = Controller(buyreg)

        stringer = Stringer()
        stringer.AddLine("You are at %s" % '')
        stringer.AddLine(CONTINUE)
        stringer.AddBuyAction(buyreg)
        stringer.AddLine(QUIT)

        result, self._alive = controller(str(stringer))

        return result


class Stringer:
    def __init__(self):
        self._string = ""

    def __str__(self):
        return self._string

    def AddBuyAction(self, buyreg):
        for key, info in buyreg:
            line = BUYMESSAGE % (key, info)
            self.AddLine(line)

    def AddLine(self, string):
        self._string += "\n"
        self._string += string


class Controller:
    def __init__(self, buyreg):
        self._buyreg = buyreg

    def __call__(self, info):
        print info
        c = None

        while c not in self._buyreg:
            c = raw_input()

            if c == "q":
                return None, False

        return self._buyreg(c), True
