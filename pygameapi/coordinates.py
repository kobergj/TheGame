from models.constants import RelativePositions as rp


class CoordinateHandler:
    # NOTE: Returns currently TopLeft Coordinates always
    # EXTRANOTE: Should be configurable, though :)
    def __init__(self, maxsize):
        self._height = maxsize[1]
        self._width = maxsize[0]

        self._registered = {}

    def Reset(self):
        self._registered = {}

    def NewRect(self, size, position):
        self._register(size, position)
        if position == rp.TopLeft:
            return self.TopLeft(size)

        if position == rp.TopMid:
            return self.TopMid(size)

        if position == rp.TopRight:
            return self.TopRight(size)

        if position == rp.Center:
            return self.Center(size)

        if position == rp.BottomLeft:
            return self.BottomLeft(size)

        if position == rp.BottomMid:
            return self.BottomMid(size)

        if position == rp.BottomRight:
            return self.BottomRight(size)

        raise NotImplementedError

    def _register(self, size, position):
        if position not in self._registered:
            self._registered[position] = 0

        self._registered[position] += size[1]

    def TopLeft(self, size):
        x = 0
        y = self._registered[rp.TopLeft] - size[1]

        return x, y

    def TopMid(self, size):
        x = self._width / 2 - size[0] / 2
        y = self._registered[rp.TopMid] - size[1]

        return x, y

    def TopRight(self, size):
        x = self._width - size[0]
        y = self._registered[rp.TopRight] - size[1]

        return x, y

    def Center(self, size):
        x = self._width / 2 - size[0] / 2
        y = self._height / 2 + self._registered[rp.Center]

        return x, y

    def BottomLeft(self, size):
        x = 0
        y = self._height - self._registered[rp.BottomLeft]

        return x, y

    def BottomMid(self, size):
        x = self._width / 2 - size[0] / 2
        y = self._height - self._registered[rp.BottomMid]

        return x, y

    def BottomRight(self, size):
        x = self._width - size[0]
        y = self._height - self._registered[rp.BottomRight]

        return x, y
