import anomalies as ans


class Universe():
    def __init__(self, anomalieInformations):
        self.planetList = list()
        for planet in anomalieInformations['planets']:
            self.__dict__[planet['name']] = ans.Planet(planet)
            self.planetList.append(planet['name'])
