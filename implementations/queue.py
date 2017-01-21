

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
