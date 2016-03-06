import math
import Queue


class Universe():
    # I guess this not right here...
    mapIdentifiers = {'Empty': '',
                      'Planet': '(00)',
                      'Spacegate': '[00]',
                      'Starbase': '$00$',
                      }

    def __init__(self, minCoordinates, maxCoordinates):
        # Init Anomaly List
        self.anomalyList = dict()

        # Init Queue - One For all Anomalies?
        self.anomalyQ = Queue.Queue(maxsize=10)

        # Draw Universe Map
        self.Map = self.drawUniverseMap(minCoordinates, maxCoordinates)

    def addAnomaly(self, Anomaly):
        # Append to Anomaly List
        self.anomalyList.update({Anomaly.name: Anomaly})

        # update Map
        x = Anomaly.coordinates[0]
        y = Anomaly.coordinates[1]

        self.Map[y][x] = Anomaly.name

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

    def drawUniverseMap(self, minCoordinates, maxCoordinates):
        universeExpansion_x = maxCoordinates[0] - minCoordinates[0]
        universeExpansion_y = maxCoordinates[1] - minCoordinates[1]

        universeMap = list()

        # Problems with negative Coordinates
        # Currently 2-Dims Only
        for j in range(universeExpansion_y + 1):
            row = list()
            for i in range(universeExpansion_x + 1):
                point_in_space = None

                # for anomaly in self.anomalyList.itervalues():
                #     if anomaly.coordinates == [j, i]:
                #         point_in_space = anomaly.name

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
