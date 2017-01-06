import implementations.container as c


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
    def __init__(self, name, cargo=[]):
        self.name = name
        self.cargo = c.Container(cargo)


class Universe(BaseModel):
    def __init__(self, name, harbors, cargos):
        self.name = name
        self.harbors = c.Container(harbors)
        self.cargos = c.Container(cargos)


class Cargo(BaseModel):
    def __init__(self, name):
        self.name = name


class Currency(BaseModel):
    def __init__(self, name):
        self.name = name


class Player(BaseModel):
    def __init__(self, name, startCurrency=0):
        self.name = name

        self.cargo = c.Container()
        self.currency = c.Container(startCurrency)
