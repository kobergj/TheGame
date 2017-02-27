from models.constants import WidgetStatus as ws

import pygame

import helpers.logger as log

MOVEMENTSPEED = 50


class Sprite(pygame.sprite.Sprite):
    # @log.Logger('InitializeSprite')
    def __init__(self, imgsrcstrategy, imgbuilder):
        pygame.sprite.Sprite.__init__(self)

        self.imgsrcstrategy = imgsrcstrategy
        self._imgbuilder = imgbuilder

        self.status = ws.Passive

        log.DebugLog('Getting Rect Size')
        self.rect = self.image.get_rect()

    @property
    def image(self):
        log.DebugLog('Getting Status for Image')
        st = self.status
        if st not in self.imgsrcstrategy:
            st = ws.Passive

        log.DebugLog('Calculating Image')
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

    def UpdateStrategy(self, imgstrategy):
        self.imgsrcstrategy = imgstrategy

    def ContainsCoordinates(self, coordinates):
        return self.rect.collidepoint(coordinates)

    def SetPassive(self):
        self.status = ws.Passive

    def SetHighlighted(self):

        if self.Validate():
            self.status = ws.Highlighted
            return

        self.status = ws.Blocked

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
    def __init__(self, imgstrategy, imgbuilder, func=None, validator=None):
        Sprite.__init__(self, imgstrategy, imgbuilder)
        self._func = func
        self._validator = validator

    def Execute(self, args=[]):
        if not self._func:
            return

        return self._func(*args)

    def Validate(self, args=[]):
        if not self._validator:
            return

        return self._validator(*args)


class ChildSprite(Sprite):
    def __init__(self, imgstrategy, imgbuilder, parent, args=[]):
        Sprite.__init__(self, imgstrategy, imgbuilder)
        self._args = args
        self._parent = parent

    def Execute(self):
        return self._parent.Execute(self._args)

    def Validate(self):
        return self._parent.Validate(self._args)
