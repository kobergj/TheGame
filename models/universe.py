import anomalies as ans
import math


class Universe():
    def __init__(self, anomalieInformations):
        self.anomalyList = list()

        self.planetList = list()
        for planet in anomalieInformations['planets']:
            self.__dict__[planet['name']] = ans.Planet(planet)
            self.planetList.append(planet['name'])
            self.anomalyList.append(planet['name'])

        for anomaly in self.anomalyList:
            self.listDistances(self.__dict__[anomaly])

    def listDistances(self, currentAnomaly):
        currentAnomaly.distances = dict()

        for anomalyName in self.anomalyList:
            anomaly = self.__dict__[anomalyName]
            distance = self.calculateDistance(currentAnomaly.coordinates, anomaly.coordinates)
            currentAnomaly.distances.update({anomalyName: distance})

    def calculateDistance(self, point1, point2):
        x0 = point1[0]
        x1 = point2[0]

        y0 = point1[1]
        y1 = point2[1]

        z0 = point1[2]
        z1 = point2[2]

        distance = (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2
        distance = math.sqrt(float(distance))

        return distance
