import implementations.container as c
import implementations.queue as q

QUEUECAP = 5


class BaseModel:
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
