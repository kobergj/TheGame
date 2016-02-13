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
            self.updateDistances(self.__dict__[anomaly])

        self.Map = self.drawUniverseMap(anomalieInformations)

    def updateDistances(self, currentAnomaly):
        for anomalyName in self.anomalyList:
            anomaly = self.__dict__[anomalyName]
            distance = self.calculateDistance(currentAnomaly.coordinates, anomaly.coordinates)
            currentAnomaly.distances.update({anomalyName: distance})

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

        for i in range(universeExpansion_y):
            row = list()
            for j in range(universeExpansion_x):
                point_in_space = ''

                for planet_info in universeInformation['Planets']:
                    if planet_info['coordinates'] == [j, i]:
                        point_in_space = planet_info['name']

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
