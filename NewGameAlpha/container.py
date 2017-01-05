import logger as h


class Container:
    def __init__(self, capacity=0):
        self._cap = capacity
        self._items = dict()

    def __getitem__(self, item):
        return self._items[str(item)]

    def __iter__(self):
        for item, amount in self._items.values():
            if amount > 0:
                yield item

    def __add__(self, item):
        return self.manipulate(item, 1)

    def __sub__(self, item):
        return self.manipulate(item, -1)

    def __int__(self):
        return self._cap

    @h.Logger('Manipulate Container')
    def manipulate(self, item, amount):
        self._cap -= amount

        key = str(item)
        if key in self._items:
            self._items[key][1] = self._items[key][1] + amount
        else:
            self._items[key] = [item, amount]

        return self._items[key]
