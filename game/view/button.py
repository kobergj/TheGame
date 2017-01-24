

class Button:
    def __init__(self, txtswitch, colswitch, rect, txtcordfunc):
        self._rect = rect
        self._colswitch = colswitch
        self._textswitch = txtswitch

        self.TextCoordinates = txtcordfunc

    def Rect(self, *switchargs):
        col = self._colswitch(self._rect, *switchargs)
        return self._rect, col

    def Text(self, *switchargs):
        return self._textswitch(*switchargs)

    def Active(self):
        return self._colswitch.active

    def DeActivate(self):
        self._colswitch.deactivate()


class TextButton:
    def __init__(self, txt, colorswitch, txtcordfunc):
        self._text = txt
        self._colors = colorswitch

        self.Coordinates = txtcordfunc

    def Text(self):
        return self._text

    def Color(self, *switchargs):
        return self._colors(*switchargs)

    def Active(self):
        return self._colors.active

    def DeActivate(self):
        self._colors.deactivate()
