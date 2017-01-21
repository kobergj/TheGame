import pygameapi as pg
import fabric as f

import implementations.registry as r
import models.models as m


BUTTONSIZE = 300, 30

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
SOME, SOMEELSE = (123, 12, 178), (30, 200, 96)

CLICKABLE = m.Switch(BLACK)

UNCLICKABLE = m.Switch(BLACK)


class View:
    def __init__(self, wsize, bsize, fontname, fontsize, bgcolor):
        self._pygameapi = pg.PyGameApi(wsize, fontname, fontsize, bgcolor)
        self._brbuilder = ButtonRegistryBuilder(wsize, self._pygameapi.GetMouse())

    def Register(self, position, msg, func, *args):
        if func:
            return self._brbuilder.RegisterClickable(position, msg, func, *args)

        return self._brbuilder.RegisterUnClickable(position, msg)

    def __call__(self):
        reg = self._brbuilder.GetRegistry()

        with self._pygameapi as api:

            for button, _ in reg:
                api.RegisterButton(button)
                if button.Active():
                    reg(button)
                button.DeActivate()

        self._brbuilder.Reset()


class ButtonRegistryBuilder:
    def __init__(self, wsize, mouse):
        self._wsize, self._mouse, self._reg = wsize, mouse, None
        self.Reset()

    def Reset(self):
        buttonfabric = f.ButtonFabric(self._wsize, self._mouse)
        self._reg = r.ExecRegistry(buttonfabric)

    def RegisterClickable(self, position, msg, func, *args):
        self._reg.Register(
            m.ButtonInfo(
                texts=m.Switch([msg, WHITE], on_highlight=[msg, SOMEELSE]),
                colors=CLICKABLE,
                position=position,
                size=BUTTONSIZE,
            ),
            func, *args
        )

    def RegisterUnClickable(self, position, msg):
        i = m.ButtonInfo(
            texts=m.Switch([msg, WHITE]),
            colors=UNCLICKABLE,
            position=position,
            size=BUTTONSIZE,
        )
        self._reg.Register(i, lambda: None)

    def GetRegistry(self):
        return self._reg
