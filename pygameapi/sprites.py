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
        self._move()

    def SetWay(self, start, end=None):
        if not end:
            end = start

        self._settopleft(start)
        self._setendpoint(end)

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

    def Validate(self):
        return True

    def Execute(self):
        return None

    def _settopleft(self, topleft):
        self.rect.topleft = topleft

    def _setendpoint(self, end):
        self._end = end

    def _move(self):
        # X - Offset
        x = self._getoffset(self.rect.x, self._end[0])
        # Y - Offset
        y = self._getoffset(self.rect.y, self._end[1])

        self.rect.move_ip(x, y)

    def _getoffset(self, actual, desired):
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

    def ExecuteChild(self, args):
        if not self._func:
            return

        return self._func(*args)

    def ValidateChild(self, args=[]):
        if not self._validator:
            return

        return self._validator(*args)


class ChildSprite(Sprite):
    def __init__(self, imgstrategy, imgbuilder, parent, args=[]):
        Sprite.__init__(self, imgstrategy, imgbuilder)
        self._args = args
        self._parent = parent

    def Execute(self):
        if self.status == ws.Blocked:
            return

        return self._parent.ExecuteChild(self._args)

    def Validate(self):
        return self._parent.ValidateChild(self._args)
