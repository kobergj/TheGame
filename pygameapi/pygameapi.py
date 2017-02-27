import pygame

import window as w
import eventhandler as eh

import helpers.logger as log
from models.constants import RelativePositions as rp


class PyGameApi:
    def __init__(self, size, font, fontsize, bgcolor):
        pygame.init()

        self._window = w.PyGameWindow(size)
        self._font = PyGameFont(font, fontsize)

        self._eventhandler = eh.PyGameEventHandler(self._window.sprites, self._window.Reset)

        self.bgcolor = bgcolor
        self._window.Fill(self.bgcolor)

    @log.Logger('Pygame Update')
    def Update(self):
        self._eventhandler()
        self._window.Update()

    def SetTopLeft(self, *spriteargs, **spritekwargs):
        return self._check(rp.TopLeft, *spriteargs, **spritekwargs)

    def SetTopMid(self, *spriteargs, **spritekwargs):
        return self._check(rp.TopMid, *spriteargs, **spritekwargs)

    def SetTopRight(self, *spriteargs, **spritekwargs):
        return self._check(rp.TopRight, *spriteargs, **spritekwargs)

    def SetMidLeft(self, *spriteargs, **spritekwargs):
        return self._check(rp.MidLeft, *spriteargs, **spritekwargs)

    def SetCenter(self, *spriteargs, **spritekwargs):
        return self._check(rp.Center, *spriteargs, **spritekwargs)

    def SetMidRight(self, *spriteargs, **spritekwargs):
        return self._check(rp.MidRight, *spriteargs, **spritekwargs)

    def SetBottomLeft(self, *spriteargs, **spritekwargs):
        return self._check(rp.BottomLeft, *spriteargs, **spritekwargs)

    def SetBottomMid(self, *spriteargs, **spritekwargs):
        return self._check(rp.BottomMid, *spriteargs, **spritekwargs)

    def SetBottomRight(self, *spriteargs, **spritekwargs):
        return self._check(rp.BottomRight, *spriteargs, **spritekwargs)

    def _check(self, position, imgstrategy, parent=None, func=None, validator=None, args=[]):
        # Is Sprite there?
        sprite = self._window.FindSpriteByImageSource(imgstrategy)
        if sprite:
            sprite.UpdateStrategy(imgstrategy)
            return sprite

        # If it has no parent - it is a parent
        if not parent:
            return self._window.NewParent(position, imgstrategy, self._renderfont, func, validator)

        return self._window.NewChild(position, imgstrategy, self._renderfont, parent, args)

    def _renderfont(self, txt, col):
        return self._font.Render(txt, col)


class PyGameFont:
    def __init__(self, fontname, fontsize):
        self._font = pygame.font.SysFont(fontname, fontsize)

    def Render(self, text, color):
        return self._font.render(text, True, color)

    def Size(self, text):
        return self._font.size(text)
