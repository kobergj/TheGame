import fabric as f
import coordinates as c

import implementations.registry as r
import models.models as m


class View:
    def __init__(self, wsize, margin):
        self._brbuilder = ButtonRegistryBuilder(wsize, margin)

    def RegisterTopMid(self, col, msg, func, args=[]):
        return self._brbuilder.Register(c.TOPMID, col, msg, func, args)

    def RegisterBottomLeft(self, col, msg, func, args=[]):
        return self._brbuilder.Register(c.BOTTOMLEFT, col, msg, func, args)

    def RegisterBottomMid(self, col, msg, func, args=[]):
        return self._brbuilder.Register(c.BOTTOMMID, col, msg, func, args)

    def RegisterBottomRight(self, col, msg, func, args=[]):
        return self._brbuilder.Register(c.BOTTOMRIGHT, col, msg, func, args)

    def __call__(self):
        reg = self._brbuilder.GetRegistry()
        self._brbuilder.Reset()
        return reg


class ButtonRegistryBuilder:
    def __init__(self, wsize, margin):
        self._wsize, self._reg, self._margin = wsize, None, margin
        self.Reset()

    def Reset(self):
        buttonfabric = f.TextButtonFabric(self._wsize, self._margin)
        self._reg = r.ExecRegistry(buttonfabric)

    def Register(self, position, colors, msg, func, args):
        self._reg.Register(
            m.ButtonInfo(
                text=msg,
                colors=m.Switch(*colors),
                position=position,
            ),
            func, *args
        )

    def GetRegistry(self):
        return self._reg
