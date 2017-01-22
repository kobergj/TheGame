import implementations.container as c
import implementations.queue as q
import implementations.counter as s

import helpers.kindaconfiguration as conf
# Configuration Access
QUEUECAP = conf.Limits.HarborCache
# Configuration Access End


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


class Ship(BaseModel):
    def __init__(self, name, statdict):
        self.name = name
        self.stats = s.StatServer(statdict)


class Player(BaseModel):
    def __init__(self, name, startCurrency):
        self.name = name

        self.cargo = c.Container()
        self.currency = c.Container(startItems=startCurrency)


class Fleet:
    def __init__(self, ships=[]):
        self.stats = s.StatServer()
        self.activeships = c.Container()
        self.standbyships = c.Container(ships)


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
