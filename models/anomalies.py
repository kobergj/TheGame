# Contains Planet Data


class Anomaly():
    # Generic Anomaly in Space.
    def __init__(self, anomalieInformation):
        self.coordinates = anomalieInformation['coordinates']


class Planet(Anomaly):
    def __init__(self, planetInformation):
        Anomaly.__init__(self, planetInformation)

        self.Name = planetInformation['name']

        self.goodsConsumed = planetInformation['goodsConsumed']
        self.goodsProduced = planetInformation['goodsProduced']
