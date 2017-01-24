import pygame
import time


class PyGameApi:
    def __init__(self, size, font, fontsize, bgcolor):
        self._eventhandler = PyGameEventHandler()
        self._window = PyGameWindow(size)
        self._mouse = PyGameMouse()
        self._font = PyGameFont(font, fontsize)

        self.bgcolor = bgcolor

    def __call__(self, buttonregistry):
        self._eventhandler()
        self._window.Fill(self.bgcolor)

        for button, _ in buttonregistry:
            self.RegisterTextButton(button)
            if button.Active():
                buttonregistry(button)
            button.DeActivate()

        self._window.Update()

    def GetMouse(self):
        return self._mouse

    def RegisterTextButton(self, txtbut):
        text = txtbut.Text()
        size = self._font.Size(text)
        rect = txtbut.Coordinates(size) + size
        col = txtbut.Color(rect, self._mouse.IsOver, self._mouse.IsPressed)
        self._window.DrawText(self._font.Render(text, col), rect)

    def RegisterButton(self, button):
        rect, rectcolor = button.Rect(self._mouse.IsOver, self._mouse.IsPressed)
        self._window.DrawRectangle(rect, rectcolor)

        text, textcolor = button.Text(rect, self._mouse.IsOver, self._mouse.IsPressed)
        size = self._font.Size(text)
        pos = button.TextCoordinates(size)
        self._window.DrawText(self._font.Render(text, textcolor), pos)


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

    def DrawText(self, txtimage, topleft):
        self._screen.blit(txtimage, topleft)

    def Update(self):
        pygame.display.flip()
        time.sleep(0.1)


class PyGameFont:
    def __init__(self, fontname, fontsize):
        self._font = pygame.font.SysFont(fontname, fontsize)

    def Render(self, text, color):
        return self._font.render(text, True, color)

    def Size(self, text):
        return self._font.size(text)


class PyGameMouse:
    def __init__(self):
        self._mouse = pygame.mouse

    def IsOver(self, rect):
        rx, ry, w, h = rect

        x, y = self._mouse.get_pos()

        if rx <= x <= rx + w and ry <= y <= ry + h:
            return True

        return False

    def IsPressed(self, rect):
        return self._mouse.get_pressed()[0]
