

class Button:
    def __init__(self, txtswitch, colswitch, rect, txtcordfunc):
        self._rect = rect
        self._colswitch = colswitch
        self._textswitch = txtswitch

        self.TextCoordinates = txtcordfunc

    def Rect(self):
        col = self._colswitch(self._rect)
        return self._rect, col

    def Text(self):
        return self._textswitch(self._rect)

    def Active(self):
        return self._colswitch.active

    def DeActivate(self):
        self._colswitch.deactivate()
