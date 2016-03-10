import math
import Queue
import random


class Universe():
    def __init__(self, minCoordinates, maxCoordinates):
        # Init Anomaly List
        self.anomalyList = dict()

        # Init Queues
        self.anomalyQ = Queue.Queue(maxsize=3)
        self.enemyQ = Queue.Queue(maxsize=3)
        self.shipQ = Queue.Queue(maxsize=3)
        self.roomQ = Queue.Queue(maxsize=3)

        # Draw Universe Map
        self.Map = self.drawUniverseMap(minCoordinates, maxCoordinates)

    def addAnomaly(self, Anomaly):
        # Append to Anomaly List
        self.anomalyList.update({Anomaly.name: Anomaly})

        # Genrate Coordinates
        x = random.randint(0, len(self.Map[0])-1)
        y = random.randint(0, len(self.Map)-1)

        # Check if already used
        while self.Map[y][x]:
            # Create New Ones
            x = random.randint(0, len(self.Map[0])-1)
            y = random.randint(0, len(self.Map)-1)

        self.Map[y][x] = Anomaly.name

        Anomaly.getCoordinates([x, y])

    def generateDistanceDict(self, currentCoordinates):
        # Init Distance Dict
        distances = dict()
        # Loop through Anomalies
        for anomaly in self.anomalyList.itervalues():
            # Calculate Distance
            distance = self.calculateDistance(currentCoordinates, anomaly.coordinates)
            # Update Distance Dist
            distances.update({anomaly.name: distance})

        return distances

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
        for j in range(universeExpansion_y):
            row = list()
            for i in range(universeExpansion_x):
                point_in_space = None

                # for anomaly in self.anomalyList.itervalues():
                #     if anomaly.coordinates == [j, i]:
                #         point_in_space = anomaly.name

                row.append(point_in_space)

            universeMap.append(row)

        return universeMap
