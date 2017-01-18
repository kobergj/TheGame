import switch as s
import fabric as f


BLACK, WHITE = (0, 0, 0), (255, 255, 255)
SOME, SOMEELSE = (123, 12, 178), (30, 200, 96)


class Button:
    def __init__(self, text, rect, colswitch):
        self._text = text
        self._rect = rect
        self._colswitch = s.MouseStateSwitch(self._rect, colswitch)

    def Rect(self):
        return self._rect

    def Text(self):
        return self._text

    def Color(self, mouse):
        return self._colswitch(mouse)

    def Active(self):
        return self._colswitch.active

    def DeActivate(self):
        self._colswitch.deactivate()


class ButtonKeys:
    def __init__(self, windowsize, buttonsize):
        self._recthandler = f.RectFabric(windowsize, buttonsize)

    def __call__(self, info):
        rect = self._recthandler()
        return Button(info.text, rect, info.switch)


class Info:
    def __init__(self, text, colscheme):
        self.text = text
        self.switch = colscheme
