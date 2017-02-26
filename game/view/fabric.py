import button as b
import switch as s
import coordinates as c


class TextButtonFabric:
    def __init__(self, windowsize, margin):
        self._cordfabric = c.TextCoordsFabric(windowsize, margin)

    def __call__(self, info):
        txtcords = self._cordfabric(info.position)
        colors = s.SwitchExecutor(info.colors)
        return b.TextButton(info.text, colors, txtcords)
