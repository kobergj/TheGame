
class BaseModel:
    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


class Action(BaseModel):
    def __init__(self, name, options, execfunc):
        self.name = name
        self.options = options
        self.execfunc = execfunc


class Harbor(BaseModel):
    def __init__(self, name, cargo):
        self.name = name
        self.cargo = cargo


class Universe(BaseModel):
    def __init__(self, name, harbornames, cargonames):
        self.name = name
        self.harbornames = harbornames
        self.cargonames = cargonames


class Cargo(BaseModel):
    def __init__(self, name, price=0):
        self.name = name
        self.price = price


class Currency(BaseModel):
    def __init__(self, name):
        self.name = name


class Player(BaseModel):
    def __init__(self, name):
        self.name = name
