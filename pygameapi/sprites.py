from models.constants import WidgetStatus as ws

import pygame

MOVEMENTSPEED = 5


class Sprite(pygame.sprite.Sprite):
    def __init__(self, imgsrcstrategy, imgbuilder):
        pygame.sprite.Sprite.__init__(self)

        self._imgsrcstrategy = imgsrcstrategy
        self._imgbuilder = imgbuilder

        self.status = ws.Passive
        self.rect = self.image.get_rect()

    def get_image(self):
        st = self.status
        if st not in self.imgsrcstrategy:
            st = ws.Passive

        return self._imgbuilder(*self.imgsrcstrategy[st])

    def update(self):
        self.move()

    def SetTopLeft(self, topleft):
        self.rect.topleft = topleft

    def SetEndpoint(self, end):
        self._end = end

    def SetWay(self, start, end):
        self.SetTopLeft(start)
        self.SetEndpoint(end)

    def ContainsCoordinates(self, coordinates):
        return self.rect.collidepoint(coordinates)

    def move(self):
        # X - Offset
        x = self.getoffset(self.rect.x, self._end[0])
        # Y - Offset
        y = self.getoffset(self.rect.y, self._end[1])

        self.rect.move_ip(x, y)

    def getoffset(self, actual, desired):
        check = desired - actual
        if check in range(0 - MOVEMENTSPEED, 0 + MOVEMENTSPEED):
            return 0

        if check > 0:
            return MOVEMENTSPEED

        return -MOVEMENTSPEED


class ParentSprite(Sprite):
    def __init__(self, imgstrategy, imgbuilder, func=None):
        Sprite.__init__(self, imgstrategy, imgbuilder)
        self._func = func

    def Execute(self, args):
        if not self._func:
            return

        return self._func(*args)


class ChildSprite(Sprite):
    def __init__(self, imgstrategy, imgbuilder, parent, args=[]):
        Sprite.__init__(self, imgstrategy, imgbuilder)
        self._args = args
        self._parent = parent

    def Execute(self):
        return self._parent.Execute(self._args)
