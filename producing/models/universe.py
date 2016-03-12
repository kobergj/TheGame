import math
import Queue
import random


class Universe():
    def __init__(self, minCoordinates, maxCoordinates):
        # Init Queues
        self.anomalyQ = Queue.Queue(maxsize=3)
        self.enemyQ = Queue.Queue(maxsize=3)
        self.shipQ = Queue.Queue(maxsize=3)
        self.roomQ = Queue.Queue(maxsize=3)

        # Draw Universe Map
        self.Map = self.drawUniverseMap(minCoordinates, maxCoordinates)

    def addAnomaly(self, Anomaly):
        # Genrate Coordinates
        x = random.randint(0, len(self.Map[0])-1)
        y = random.randint(0, len(self.Map)-1)

        # Check if already used
        while self.Map[y][x]:
            # Create New Ones
            x = random.randint(0, len(self.Map[0])-1)
            y = random.randint(0, len(self.Map)-1)

        self.Map[y][x] = Anomaly

        Anomaly.getCoordinates([x, y])

    def generateDistanceDict(self, currentCoordinates):
        # Init Distance Dict
        distances = dict()
        # Loop through Slices
        for verticalSlice in self.Map:
            # Loop through Anomalies
            for anomaly in verticalSlice:
                if anomaly:
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
        for verticalSlice in range(universeExpansion_y):
            # Vertical Slices through Space
            verticalSlice = list()

            for point_in_space in range(universeExpansion_x):
                point_in_space = None

                verticalSlice.append(point_in_space)

            universeMap.append(verticalSlice)

        return universeMap

    def callAnomaly(self, Coordinates):
        verticalSlice = Coordinates[1]
        pointInSpace = Coordinates[0]

        anomaly = self.Map[verticalSlice][pointInSpace]

        return anomaly
