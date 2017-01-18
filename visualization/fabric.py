

class CoordinateFabric:
    def __init__(self, size, height):
        self._line = -height
        self._width = size[0]
        self._height = size[1]
        self._margin = height

    def __call__(self):
        # center = self._width / 2
        left = 0
        self._line += self._margin
        return left, self._line


class RectFabric:
    def __init__(self, maxsize, rectsize):
        self._cfabric = CoordinateFabric(maxsize, rectsize[1])
        self._size = rectsize

    def __call__(self):
        cords = self._cfabric()
        return (cords[0], cords[1], self._size[0], self._size[1])
