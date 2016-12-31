
class BaseModel:
    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


class Harbor(BaseModel):
    def __init__(self, name):
        self.name = name


class Space(BaseModel):
    def __init__(self, nextHarbor):
        self.name = "Space"
        self.destination = nextHarbor


class Cargo(BaseModel):
    def __init__(self, name, price=0):
        self.name = name
        self.price = price


class Currency(BaseModel):
    def __init__(self, name):
        self.name = name