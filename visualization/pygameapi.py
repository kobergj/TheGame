import pygame
import time


class PyGameApi:
    def __init__(self, size, font, fontsize, bgcolor):
        self._eventhandler = PyGameEventHandler()
        self._window = PyGameWindow(size)
        self._mouse = PyGameMouse()
        self._font = PyGameFont(font, fontsize)

        self.bgcolor = bgcolor

    def __enter__(self):
        self._eventhandler()
        self._window.Fill(self.bgcolor)
        return self

    def __exit__(self, type, value, tb):
        self._window.Update()

    def RegisterButton(self, button):
        rc, tc = button.Color(self._mouse)
        text = self._font.Render(button.Text(), tc)
        rect = button.Rect()

        self._window.DrawRectangle(rect, rc)
        self._window.DrawText(text, rect)


class PyGameEventHandler:
    def __init__(self):
        pygame.init()

    def __call__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


class PyGameWindow:
    def __init__(self, size):
        self._screen = pygame.display.set_mode(size)

    def Fill(self, color):
        self._screen.fill(color)

    def DrawRectangle(self, rect, color):
        pygame.draw.rect(
            self._screen,
            color,
            rect,
        )

    def DrawText(self, renderedfont, rect):
        self._screen.blit(renderedfont, rect)

    def Update(self):
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
