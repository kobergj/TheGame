import pygame
import time

FONTNAME = 'comicsansms'
FONTSIZE = 25
MARGIN = 30


class PyGameWindow:
    def __init__(self, size):
        pygame.init()
        self._screen = pygame.display.set_mode(size)
        self._font = pygame.font.SysFont(FONTNAME, FONTSIZE)

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def Fill(self, color):
        self._screen.fill(color)

    def DrawButton(self, button, rcol, tcol):
        txt = self._font.render(button.Text(), True, tcol)

        rect = button.Rect()
        # rect.inflate(MARGIN, MARGIN)

        self.DrawRectangle(rect, rcol)
        self.DrawText(txt, rect)

    def DrawRectangle(self, rect, color):
        pygame.draw.rect(
            self._screen,
            color,
            rect,
        )

    def DrawText(self, text, rect):
        self._screen.blit(text, rect)

    def Show(self):
        pygame.display.flip()
        time.sleep(0.1)


class PyGameFont:
    def __init__(self, fontname, fontsize):
        self._font = pygame.font.SysFont(fontname, fontsize)

    def Render(self, text, color):
        return self._font.render(text, True, color)


class PyGameMouse:
    def __init__(self):
        self._mouse = pygame.mouse

    def IsOver(self, rect):
        rx, ry, w, h = rect

        x, y = self._mouse.get_pos()

        if rx <= x <= rx + w and ry <= y <= ry + h:
            return True

        return False

    def IsPressed(self):
        return self._mouse.get_pressed()[0]


# Rect = (coords[0], coords[1], size[0], size[1])
