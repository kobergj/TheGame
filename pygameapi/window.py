import pygame
import time

import sprites as s
import coordinates as c


class PyGameWindow:
    def __init__(self, size, bgcolor=None):
        self._screen = pygame.display.set_mode(size)
        self._coordinatehandler = c.CoordinateHandler(size)

        self.sprites = pygame.sprite.Group()

        self._bg = bgcolor

    def Fill(self, color):
        self._bg = color

    def NewParent(self, position, imgstrategy, imgbuilder, func, validator):
        sprite = s.ParentSprite(imgstrategy, imgbuilder, func, validator)
        self._addsprite(sprite, position)
        return sprite

    def NewChild(self, position, imgstrategy, imgbuilder, parent, args):
        sprite = s.ChildSprite(imgstrategy, imgbuilder, parent, args)
        self._addsprite(sprite, position)
        return sprite

    def Update(self):
        self.sprites.update()
        self._drawsprites()
        pygame.display.flip()
        self._screen.fill(self._bg)
        # time.sleep(1)

    def Reset(self):
        self.sprites.empty()
        self._coordinatehandler.Reset()

    def FindSpriteByImageSource(self, imgsource):
        for sprite in self.sprites:
            if sprite.imgsrcstrategy == imgsource:
                return sprite

        return None

    def _drawsprites(self):
        self.sprites.draw(self._screen)

    def _addsprite(self, sprite, position):
        crds = self._coordinatehandler.NewRect(sprite.rect.size, position)
        sprite.SetWay(crds)

        self.sprites.add(sprite)
