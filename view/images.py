from models.constants import InteractionTypes as it, WidgetStatus as ws

import helpers.logger as log


class ImageSource:
    def __init__(self, imagepathes):
        self._imgsrc = imagepathes

    def ParentStrategy(self, typ):
        if typ == it.Buy:
            return self.BuyParent()

        if typ == it.Sell:
            return self.SellParent()

        if typ == it.Stats:
            return self.StatsParent()

        if typ == it.Travel:
            return self.TravelParent()

        if typ == it.Info:
            return self.InfoParent()

        raise NotImplementedError

    def ChildStrategy(self, typ, args=[]):
        if typ == it.Buy:
            return self.BuyChild(args)

        if typ == it.Sell:
            return self.SellChild(args)

        if typ == it.Stats:
            return self.StatsChild(args)

        if typ == it.Travel:
            return self.TravelChild(args)

        if typ == it.Info:
            return self.InfoChild(args)

        raise NotImplementedError

    def BuyParent(self):
        return ImageStrategy(it.Buy, self._imgsrc.BuyParent)

    def SellParent(self):
        return ImageStrategy(it.Sell, self._imgsrc.SellParent)

    def StatsParent(self):
        return ImageStrategy(it.Stats, self._imgsrc.StatsParent)

    def TravelParent(self):
        return ImageStrategy(it.Travel, self._imgsrc.TravelParent)

    def InfoParent(self):
        return ImageStrategy(it.Info, self._imgsrc.WelcomeParent)

    def BuyChild(self, args):
        bc = self._imgsrc.BuyChild
        imgs = ImageStrategy(it.Buy, [bc[0].format(*args), bc[1]], args)

        bhc = self._imgsrc.BuyHighlightedChild
        imgs[ws.Highlighted] = [bhc[0].format(*args), bhc[1]]

        bbc = self._imgsrc.BuyBlockedChild
        imgs[ws.Blocked] = [bbc[0].format(*args), bbc[1]]
        return imgs

    def SellChild(self, args):
        bc = self._imgsrc.SellChild
        imgs = ImageStrategy(it.Sell, [bc[0].format(*args), bc[1]], args)

        bhc = self._imgsrc.SellHighlightedChild
        imgs[ws.Highlighted] = [bhc[0].format(*args), bhc[1]]
        return imgs

    def StatsChild(self, args):
        sc = self._imgsrc.StatsChild
        imgs = ImageStrategy(it.Stats, [sc[0].format(*args), sc[1]], args)
        return imgs

    def TravelChild(self, args):
        tc = self._imgsrc.TravelChild
        imgs = ImageStrategy(it.Travel, [tc[0].format(*args), tc[1]], args)

        thc = self._imgsrc.TravelHighlightedChild
        imgs[ws.Highlighted] = [thc[0].format(*args), thc[1]]
        return imgs

    def InfoChild(self, args):
        ic = self._imgsrc.WelcomeChild
        imgs = ImageStrategy(it.Info, [ic[0].format(*args), ic[1]], args)
        return imgs


class ImageStrategy:
    @log.Logger('InitializeImageStrategy')
    def __init__(self, typ, default, args=[]):
        self.typ = typ
        self.args = args

        self._innerdict = {
            ws.Passive: default
        }

    def __getitem__(self, key):
        if key not in self._innerdict:
            key = ws.Passive

        return self._innerdict[key]

    def __setitem__(self, status, image):
        self._innerdict[status] = image

    def __contains__(self, status):
        return status in self._innerdict

    def __eq__(self, other):
        return self.typ == other.typ and self.args == other.args

    def __ne__(self, other):
        return not self.__eq__(other)
