# Contains Planet Data


class Anomaly():
    # Generic Anomaly in Space.
    # TODO: Coordinates
    def __init__(self):
        self.coordinates = [0, 0, 0]


class Planet(Anomaly):
    def __init__(self, planetInformation):
        Anomaly.__init__(self)

        self.Name = planetInformation['name']

        self.goodsConsumed = planetInformation['goodsConsumed']
        self.goodsProduced = planetInformation['goodsProduced']
