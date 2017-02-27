import pygame

import window as w
import coordinates as c
import eventhandler as eh

import helpers.logger as log


class PyGameApi:
    def __init__(self, size, font, fontsize, bgcolor):
        pygame.init()

        self._window = w.PyGameWindow(size)
        self._font = PyGameFont(font, fontsize)
        self._coordinatehandler = c.CoordinateHandler(size)

        self._eventhandler = eh.PyGameEventHandler(self._window.sprites, self._coordinatehandler.Reset)

        self.bgcolor = bgcolor
        self._window.Fill(self.bgcolor)

    @log.Logger('Pygame Update')
    def Update(self):
        self._eventhandler()
        self._window.Update()

    def CheckSprite(self, position, imgstrategy, parent=None, func=None, validator=None, args=[]):
        # Is Sprite there?
        sprite = self._window.FindSpriteByImageSource(imgstrategy)
        if sprite:
            sprite.UpdateStrategy(imgstrategy)
            return sprite

        # If it has no parent - it is a parent
        if not parent:
            return self.NewParentSprite(position, imgstrategy, func, validator)

        return self.NewChildSprite(position, imgstrategy, parent, args)

    @log.Logger('NewParentSprite')
    def NewParentSprite(self, position, imgstrategy, execfunc=None, validator=None):
        sprite = self._window.NewParent(imgstrategy, self.RenderFont, execfunc, validator)
        coordinates = self._coordinatehandler.NewRect(sprite.rect.size, position)
        sprite.SetWay(coordinates, coordinates)
        return sprite

    @log.Logger('NewChildSprite')
    def NewChildSprite(self, position, imgstrategy, parent, args=[]):
        sprite = self._window.NewChild(imgstrategy, self.RenderFont, parent, args)
        coordinates = self._coordinatehandler.NewRect(sprite.rect.size, position)
        sprite.SetWay(coordinates, coordinates)
        return sprite

    def RenderFont(self, txt, col):
        return self._font.Render(txt, col)


class PyGameFont:
    def __init__(self, fontname, fontsize):
        self._font = pygame.font.SysFont(fontname, fontsize)

    def Render(self, text, color):
        return self._font.render(text, True, color)

    def Size(self, text):
        return self._font.size(text)
