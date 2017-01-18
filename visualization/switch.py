

class MouseStateSwitch:
    def __init__(self, container, switch):
        self._container = container
        self._switch = switch
        self.active = False

    def __call__(self, mouse):
        if self.active:
            return self._switch.OnActive

        if mouse.IsOver(self._container):

            if mouse.IsPressed():
                self.active = True
                return self._switch.OnClick

            return self._switch.OnHighlight

        return self._switch.OnPassive

    def deactivate(self):
        self.active = False


class Switch:
    def __init__(self, on_passive=None, on_highlight=None, on_click=None, on_active=None):
        self.OnHighlight = on_highlight
        self.OnClick = on_click
        self.OnPassive = on_passive
        self.OnActive = on_active
