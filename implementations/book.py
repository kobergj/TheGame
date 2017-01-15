

class Book:
    def __init__(self, *pages):
        self._head = None
        self._current = None

        for data in pages:
            self.AddPage(data)

    def Read(self):
        return self._current.Read()

    def AddPage(self, data):
        pg = Page(data)
        pg.SetNext(self._head)
        self._head = pg
        self._current = pg

    def TurnPage(self):
        page = self._current.Next()

        if not page:
            page = self._head

        self._current = page


class Page:
    def __init__(self, data):
        self._data = data
        self._next = None

    def Read(self):
        return self._data

    def Next(self):
        return self._next

    def SetNext(self, nxt):
        self._next = nxt
