import switch as s


class Trigger:
    def __init__(self, coords, size, colswitch):
        self._size = size
        self._colswitch = s.MouseStateSwitch(self, colswitch)
        self.active = False
        self._crds = coords

    def activate(self):
        self.active = True

    def color(self, mouse):
        return self._colswitch(mouse)

    def change_coordinates(self, cords):
        self._crds = cords

    def change_size(self, size):
        self.size = size

    def resetcolswitch(self):
        self._colswitch.deactivate()


class RectTrigger(Trigger):
    def __contains__(self, item):
        w = self._size[0]
        h = self._size[1]

        cx = self._crds[0]
        cy = self._crds[1]

        x = item[0]  # - cx
        y = item[1]  # - cy

        if cx <= x <= cx + w and cy <= y <= cy + h:
            return True

        return False

    def draw(self, screen, col):
        if col:
            log.debug('Drawing Rectangle with color %s' % [col])
            pygame.draw.rect(screen, col, (self._crds[0], self._crds[1], self._size[0], self._size[1]))
