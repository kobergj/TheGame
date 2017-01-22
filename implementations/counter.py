

class StatServer:
    def __init__(self, stats={}):
        self._stats = stats

    def __iter__(self):
        for name, value in self._stats.iteritems():
            yield name, value

    def __setitem__(self, name, value):
        self._stats.update({name: value})

    def __iadd__(self, other):
        for name, value in other:

            if name not in self:
                self[name] = value
            else:
                self[name] += value

        return self

    def __isub__(self, other):
        for name, value in other:

            if name not in self:
                self[name] = -value
            else:
                self[name] -= value

        return self

    def __contains__(self, item):
        return item in self._stats

    def __getitem__(self, name):
        return self._stats[name]
