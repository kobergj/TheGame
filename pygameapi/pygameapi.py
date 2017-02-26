import pygame

import window as w


class PyGameApi:
    def __init__(self, size, font, fontsize, bgcolor):
        self._eventhandler = PyGameEventHandler()
        self._window = w.PyGameWindow(size)
        self._font = PyGameFont(font, fontsize)

        self.bgcolor = bgcolor
        self._window.Fill(self.bgcolor)

    def Update(self):
        self._eventhandler()
        self._window.Update()

    def NewParentSprite(self, position, imgstrategy, execfunc=None):
        sprite = self._window.NewParent(imgstrategy, self.font.Render, execfunc)
        coordinates = self._coordinatehandler.NewRect(sprite.rect.size, position)
        sprite.SetWay(coordinates, coordinates)
        return sprite

    def NewChildSprite(self, position, imgstrategy, parent, args=[]):
        sprite = self._window.NewChild(imgstrategy, self.font.Render, parent, args)
        coordinates = self._coordinatehandler.NewRect(sprite.rect.size, position)
        sprite.SetWay(coordinates, coordinates)
        return sprite

    def RenderFont(self, txt, col):
        return self._font.Render(txt, col)


class PyGameEventHandler:
    def __init__(self):
        pygame.init()

    def __call__(self):
        for event in pygame.event.get():
            self.HandleEvent(event)

    def HandleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # if event.type == pygame.MOUSEMOTION:
        #     print event.pos

        # if event.type == pygame.MOUSEBUTTONUP:
        #     print event

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print event


class PyGameFont:
    def __init__(self, fontname, fontsize):
        self._font = pygame.font.SysFont(fontname, fontsize)

    def Render(self, text, color):
        return self._font.render(text, True, color)

    def Size(self, text):
        return self._font.size(text)
