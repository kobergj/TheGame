from models.constants import InteractionTypes as it, WidgetStatus as ws


class ImageSource:
    def __init__(self, imagepathes):
        self._imgsrc = imagepathes

    def ParentStrategy(self, typ):
        if typ == it.Buy:
            return self.BuyParent()

        raise NotImplementedError

    def ChildStrategy(self, typ, args=[]):
        if typ == it.Buy:
            return self.BuyChild()

        raise NotImplementedError

    def BuyParent(self):
        return ImageStrategy(self._imgsrc.Buy.Parent)

    def BuyChild(self, args):
        imgs = ImageStrategy(self._imgrsc.Buy.Child)
        imgs[ws.Highlighted] = self._imgrsc.Buy.HighlightedChild


class ImageStrategy:
    def __init__(self, default):
        self._innerdict = {
            ws.Passive: default
        }

    def __getitem__(self, key):
        if key not in self._innerdict:
            key = ws.Passive

        return self._innerdict[key]

    def __setitem__(self, status, image):
        self._innerdict[status] = image
