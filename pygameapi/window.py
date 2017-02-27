import pygame
import time

import sprites as s


class PyGameWindow:
    def __init__(self, size, bgcolor=None):
        self._screen = pygame.display.set_mode(size)
        self.sprites = pygame.sprite.Group()

        self._bg = bgcolor

    def Fill(self, color):
        self._bg = color

    def DrawSprites(self):
        self.sprites.draw(self._screen)

    def AddSprite(self, sprite):
        self.sprites.add(sprite)

    def NewParent(self, imgstrategy, imgbuilder, func, validator):
        sprite = s.ParentSprite(imgstrategy, imgbuilder, func, validator)
        self.AddSprite(sprite)
        return sprite

    def NewChild(self, imgstrategy, imgbuilder, parent, args):
        sprite = s.ChildSprite(imgstrategy, imgbuilder, parent, args)
        self.AddSprite(sprite)
        return sprite

    def Update(self):
        self.sprites.update()
        self.DrawSprites()
        pygame.display.flip()
        self._screen.fill(self._bg)
        # time.sleep(1)

    def FindSpriteByImageSource(self, imgsource):
        for sprite in self.sprites:
            if sprite.imgsrcstrategy == imgsource:
                return sprite

        return None
