import pygame
import time

import sprites as s


class PyGameWindow:
    def __init__(self, size, bgcolor=None):
        self._screen = pygame.display.set_mode(size)
        self._sprites = pygame.sprite.Group()

        self._bg = bgcolor

    def Fill(self, color):
        self._bg = color

    def DrawSprites(self):
        self._sprites.draw(self._screen)
        self._sprites.empty()

    def AddSprite(self, sprite):
        self._sprites.add(sprite)

    def NewParent(self, imgstrategy, imgbuilder, func):
        sprite = s.ParentSprite(imgstrategy, imgbuilder, func)
        self.AddSprite(sprite)
        return sprite

    def NewChild(self, imgstrategy, imgbuilder, parent, args):
        sprite = s.ChildSprite(imgstrategy, imgbuilder, parent, args)
        self.AddSprite(sprite)
        return sprite

    def Update(self):
        self._sprites.update()
        self.DrawSprites()
        pygame.display.flip()
        self._screen.fill(self._bg)
        # time.sleep(1)

    def FindSprite(self, coordinates):
        for sprite in self._sprites:
            if sprite.ContainsCoordinates(coordinates):
                return sprite

        return None
