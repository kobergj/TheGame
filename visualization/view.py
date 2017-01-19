import pygameapi as pg
import fabric as f


class View:
    def __init__(self, wsize, bsize, fontname, fontsize, bgcolor):
        self._pygameapi = pg.PyGameApi(wsize, fontname, fontsize, bgcolor)
        self._chandler = f.CoordinateFabric(wsize, bsize[1])

    def __call__(self, reg):

        with self._pygameapi as api:

            for button, _ in reg:

                api.RegisterButton(button)

                if button.Active():
                    reg(button)

                button.DeActivate()
