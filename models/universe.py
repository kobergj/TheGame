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

        self.spacegateList = list()
        for spacegate in anomalieInformations['spacegates']:
            self.__dict__[spacegate['name']] = ans.Spacegate(spacegate)
            self.spacegateList.append(spacegate['name'])
            self.anomalyList.append(spacegate['name'])

        for anomaly in self.anomalyList:
            self.updateDistances(self.__dict__[anomaly])

        self.Map = self.drawUniverseMap(anomalieInformations)

    def updateDistances(self, currentAnomaly):
        for anomalyName in self.anomalyList:
            anomaly = self.__dict__[anomalyName]
            distance = self.calculateDistance(currentAnomaly.coordinates, anomaly.coordinates)
            currentAnomaly.distances.update({anomalyName: distance})

        if currentAnomaly.name in self.spacegateList:
            currentAnomaly.overrideDistances()

    def calculateDistance(self, point1, point2):
        distance = 0.0
        for i in range(len(point1)):
            x = point1[i]
            y = point2[i]

            distance += (x - y)**2

        distance = math.sqrt(distance)
        distance = round(distance, 2)

        return distance

    def drawUniverseMap(self, universeInformation):
        universeExpansion_x = universeInformation['maxCoordinates'][0] - universeInformation['minCoordinates'][0]
        universeExpansion_y = universeInformation['maxCoordinates'][1] - universeInformation['minCoordinates'][1]

        universeMap = list()

        # Problems with negative Coordinates
        # Currently 2-Dims Only
        for j in range(universeExpansion_y + 1):
            row = list()
            for i in range(universeExpansion_x + 1):
                point_in_space = ''

                for anomaly in self.anomalyList:
                    crds = self.__dict__[anomaly].coordinates
                    if crds == [j, i]:
                        point_in_space = anomaly

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
