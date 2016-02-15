import anomalies as ans
import math


class Universe():
    def __init__(self, anomalieInformations):
        # Init Anomaly List
        self.anomalyList = dict()

        # Init Planet List:
        self.planetList = dict()
        # Loop through Planet Informations
        for planetInformation in anomalieInformations['planets']:
            # Create Planet
            planet = ans.Planet(planetInformation)

            # Append Planet to Planet List
            self.planetList.update({planet.name: planet})

            # Append Planet to Anomaly List
            self.anomalyList.update({planet.name: planet})

        # Init Spacegate List
        self.spacegateList = dict()
        # Loop through Spacegate Information
        for spacegate in anomalieInformations['spacegates']:
            # Create Spacegate
            spacegate = ans.Spacegate(spacegate)

            # Append Spacegate to Spacegate List
            self.spacegateList.update({spacegate.name: spacegate})

            # Append Spacegate to Anomaly List
            self.anomalyList.update({spacegate.name: spacegate})

        # Draw Universe Map
        self.Map = self.drawUniverseMap(anomalieInformations)

    def updateDistances(self, Ship, currentCoordinates):
        # Reset Distances
        Ship.distances = dict()
        # Loop through Anomalies
        for anomaly in self.anomalyList.itervalues():
            # Calculate Distance
            distance = self.calculateDistance(currentCoordinates, anomaly.coordinates)
            # Update Distance Dist
            Ship.distances.update({anomaly.name: distance})

        # if currentAnomaly.name in self.spacegateList:
        #     currentAnomaly.overrideDistances()

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

                for anomaly in self.anomalyList.itervalues():
                    if anomaly.coordinates == [j, i]:
                        point_in_space = anomaly.name

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
