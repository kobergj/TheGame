import button as b
import switch as s

TOPLEFT = 0
TOPMID = 1
TOPRIGHT = 2
BOTTOMLEFT = 3
BOTTOMMID = 4
BOTTOMRIGHT = 5


class ButtonFabric:
    def __init__(self, windowsize, mouse):
        self._cordfabric = CoordinateFabric(windowsize)
        self._mouse = mouse

    def __call__(self, info):
        x, y, txtcords = self._cordfabric(info.size, info.position)

        texts = s.MouseTrigger(info.texts, self._mouse)
        colors = s.MouseTrigger(info.colors, self._mouse)
        return b.Button(texts, colors, (x, y) + info.size, txtcords)


class CoordinateFabric:
    def __init__(self, maxsize):
        self._height = maxsize[1]
        self._width = maxsize[0]

        self._registered = {}

    def __call__(self, size, position):
        self._register(size, position)
        if position == TOPLEFT:
            return self.TopLeft(size)

        if position == TOPMID:
            return self.TopMid(size)

        if position == TOPRIGHT:
            return self.TopRight(size)

        if position == BOTTOMLEFT:
            return self.BottomLeft(size)

        if position == BOTTOMMID:
            return self.BottomMid(size)

        if position == BOTTOMRIGHT:
            return self.BottomRight(size)

        raise NotImplementedError

    def _register(self, size, position):
        if position not in self._registered:
            self._registered[position] = 0

        self._registered[position] += size[1]

    def TopLeft(self, size):
        x = 0
        y = self._registered[TOPLEFT] - size[1]

        def txtcords(txtsize):
            return x, y

        return x, y, txtcords

    def TopMid(self, size):
        x = self._width / 2 - size[0] / 2
        y = self._registered[TOPMID] - size[1]

        def txtcords(txtsize):
            return self._width / 2 - txtsize[0] / 2, y

        return x, y, txtcords

    def TopRight(self, size):
        x = self._width - size[0]
        y = self._registered[TOPRIGHT] - size[1]

        def txtcords(txtsize):
            return self._width - txtsize[0], y

        return x, y, txtcords

    def BottomLeft(self, size):
        x = 0
        y = self._height - self._registered[BOTTOMLEFT]

        def txtcords(txtsize):
            return x, y

        return x, y, txtcords

    def BottomMid(self, size):
        x = self._width / 2 - size[0] / 2
        y = self._height - self._registered[BOTTOMMID]

        def txtcords(txtsize):
            return self._width / 2 - txtsize[0] / 2, y

        return x, y, txtcords

    def BottomRight(self, size):
        x = self._width - size[0]
        y = self._height - self._registered[BOTTOMRIGHT]

        def txtcords(txtsize):
            return self._width - txtsize[0], y

        return x, y, txtcords


class RectFabric:
    def __init__(self, maxsize, rectheight):
        self._cfabric = CoordinateFabric(maxsize, rectheight)

    def __call__(self, size, position):
        cords = self._cfabric(self._rectsize, position)
        return (cords[0], cords[1], self._rectsize[0], self._rectsize[1])
