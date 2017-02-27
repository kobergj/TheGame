import pygame


class PyGameEventHandler:
    def __init__(self, sprites, cordsreset):
        self.sprites = sprites
        self._reset = cordsreset

    def __call__(self):
        for event in pygame.event.get():
            self.HandleEvent(event)

    def HandleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION:
            self.HandleMotion(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.HandleClick(event.pos)

    def HandleMotion(self, pos):
        for sprite in self.sprites:
            sprite.SetPassive()

            if sprite.ContainsCoordinates(pos):
                sprite.SetHighlighted()

        return

    def HandleClick(self, pos):
        for sprite in self.sprites:

            if sprite.ContainsCoordinates(pos):
                sprite.Execute()
                self._reset()
                return

        return
