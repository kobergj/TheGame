

class MouseTrigger:
    def __init__(self, switch, mouse):
        self._switch = switch
        self._mouse = mouse
        self.active = False

    def __call__(self, rect):
        if self.active:
            return self._switch.OnActive

        if self._mouse.IsOver(rect):

            if self._mouse.IsPressed():
                self.active = True
                return self._switch.OnClick

            return self._switch.OnHighlight

        return self._switch.OnPassive

    def deactivate(self):
        self.active = False
