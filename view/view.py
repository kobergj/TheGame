
CONTINUE = "[ENTER] Continue"
QUIT = "[q] Quit Game"


class ViewInterface:
    def __init__(self):
        self._stringer = Stringer()
        self._alive = True

    def __call__(self, logicInterface):
        buyoptions = logicInterface.CargoBuyOptions()

        controller = Controller(buyoptions)

        self.AddBuyOptions(buyoptions)

        self._alive = controller(str(self._stringer))

    def __nonzero__(self):
        return self._alive

    def AddBuyOptions(self, buyoptions):
        # Continue
        c = CONTINUE
        self._stringer.AddLine(c)

        # Buy
        self._stringer.AddAction(buyoptions)

        # Quit
        q = QUIT
        self._stringer.AddLine(q)


class Stringer:
    def __init__(self):
        self._string = ""

    def __str__(self):
        return self._string

    def AddAction(self, action):
        for i, option in enumerate(action.options):
            line = "[%s] " % i + str(action) % (str(option[0]), option[1])
            self.AddLine(line)

    def AddLine(self, string):
        self._string += "\n"
        self._string += string


class Controller:
    def __init__(self, options):
        self._options = options

    def __call__(self, info):
        print info
        c = -1

        while not 0 < int(c) <= len(self._options.options):
            c = raw_input()

            if c == "q":
                return False

        self._options.execfunc(int(c) - 1)
        return True
