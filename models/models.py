import implementations.container as c
import implementations.queue as q

QUEUECAP = 5


class BaseModel:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)


class Harbor(BaseModel):
    def __init__(self, name, cargo):
        self.name = name
        self.cargo = c.Container(startItems=cargo)


class Universe(BaseModel):
    def __init__(self, name, harborfactory):
        self.name = name
        self.harbors = q.RefillingQueue(harborfactory, cache=QUEUECAP)


class Cargo(BaseModel):
    def __init__(self, name):
        self.name = name


class Currency(BaseModel):
    def __init__(self, name):
        self.name = name


class Player(BaseModel):
    def __init__(self, name, startCurrency):
        self.name = name

        self.cargo = c.Container()
        self.currency = c.Container(startItems=startCurrency)


class ButtonInfo:
    def __init__(self, texts, colors, size, position):
        self.texts = texts
        self.colors = colors
        self.position = position
        self.size = size


class Switch:
    def __init__(self, on_passive, on_highlight=None, on_click=None, on_active=None):
        self.OnPassive = on_passive

        self.OnHighlight = on_passive
        if on_highlight:
            self.OnHighlight = on_highlight

        self.OnClick = on_passive
        if on_click:
            self.OnClick = on_click

        self.OnActive = on_passive
        if on_active:
            self.OnActive = on_active
