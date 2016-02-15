import models.anomalies as ans
import math


class Universe():
    def __init__(self, universeInformations):
        # Extract Anomaly Informations:
        anomalyClasses = universeInformations['anomalyInformations']
        # Init Anomaly List
        self.anomalyList = dict()

        # Loop through Anomaly Classes
        for anomalyClass, anomalyInformationList in anomalyClasses.iteritems():
            # Loop through Anomalies
            for anomalyInformation in anomalyInformationList:
                # Create Anomaly
                anomaly = ans.__dict__[anomalyClass](anomalyInformation)

                # Append Anomaly to Anomaly List
                self.anomalyList.update({anomaly.name: anomaly})

        # Draw Universe Map
        self.Map = self.drawUniverseMap(universeInformations)

    def updateDistances(self, Ship, currentCoordinates):
        # Reset Distances
        Ship.distances = dict()
        # Loop through Anomalies
        for anomaly in self.anomalyList.itervalues():
            # Calculate Distance
            distance = self.calculateDistance(currentCoordinates, anomaly.coordinates)
            # Update Distance Dist
            Ship.distances.update({anomaly.name: distance})

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
                point_in_space = None

                for anomaly in self.anomalyList.itervalues():
                    if anomaly.coordinates == [j, i]:
                        point_in_space = anomaly.name

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
