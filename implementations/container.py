import helpers.logger as h


class Container:
    def __init__(self, capacity=0, startItems=[]):
        self._cap = capacity
        self._items = dict()

        for item, amount in startItems:
            self.manipulate(item, amount)

    def __getitem__(self, item):
        return self._items[item]

    def __iter__(self):
        for item, amount in self._items.iteritems():
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

        # key = str(item)
        if item in self._items:
            self._items[item] += amount
        else:
            self._items[item] = amount

        return item, self._items[item]
