import pygameapi as pg
import fabric as f

FONTNAME, FONTSIZE = 'comicsansms', 25

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
SOME, SOMEELSE = (123, 12, 178), (30, 200, 96)


class View:
    def __init__(self, wsize, bsize):
        self._window = pg.PyGameWindow(wsize)
        self._mouse = pg.PyGameMouse()
        self._font = pg.PyGameFont(FONTNAME, FONTSIZE)
        self._chandler = f.CoordinateFabric(wsize, bsize[1])

    def __call__(self, reg):
        self._window.Fill(WHITE)
        for button, text in reg:
            rc, tc = button.Color(self._mouse)
            self._window.DrawButton(button, rc, tc)
            if button.Active():
                reg(button)
            button.DeActivate()
        self._window.Show()

    def Handle(self):
        self._window.HandleEvents()
