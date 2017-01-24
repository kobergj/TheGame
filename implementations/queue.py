

class RefillingQueue:
    def __init__(self, factory, cache=0):
        self._lifeline = list()
        self._factory = factory
        self._current = factory()

        for _ in range(cache):
            self.Add()

    def Get(self, amount=1):
        yield self.Current()
        for i in range(1, amount):
            yield self.Shift()

    def Set(self, item):
        self._current = item
        self.Refill()

    def Refill(self):
        i = len(self._lifeline)
        self._lifeline = []
        for _ in range(i):
            self.Add()

    def LookUp(self, index=1):
        return self._lifeline[:index]

    def Shift(self):
        self.Add()
        self._current = self._lifeline.pop(0)
        return self.Current()

    def Current(self):
        return self._current

    def Add(self):
        item = self._factory()
        while item in self._lifeline:
            item = self._factory()
        self._lifeline.append(item)


class ActivationQueue:
    def __init__(self, start=[]):
        self._activeItems = []
        self._standbyItems = []
        for item in start:
            self.Add(item)
            self.Activate(item)

    def Add(self, item):
        self._standbyItems.append(item)

    def Activate(self, item):
        self._standbyItems.remove(item)
        item()
        self._active.append(item)
