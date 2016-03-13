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

        # Coordinates Cursor
        self.coCursor = [-1, 0]

    def __iter__(self):
        return self

    def __getitem__(self, coordinates):
        vSlice = coordinates[1]
        point = coordinates[0]

        return self.Map[vSlice][point]

    def next(self):
        anomaly = None
        # print self.coCursor
        while not anomaly:
            self.coCursor[0] += 1
            if self.coCursor[0] >= len(self.Map[self.coCursor[1]]):
                self.coCursor[0] = -1
                self.coCursor[1] += 1

            if self.coCursor[1] >= len(self.Map):
                self.coCursor = [-1, 0]
                raise StopIteration

            anomaly = self[self.coCursor]

        return anomaly

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

    # def callNextAnomaly(self, currentPosition):
    #     # Set starting Slice
    #     startingSlice = currentPosition[1]
    #     # Loop through bigger Slices
    #     for verticalSlice in self.Map[startingSlice:]:
    #         # Set starting point
    #         startingPoint = currentPosition[0] + 1
    #         # Loop through anomalies
    #         for anomaly in verticalSlice[startingPoint:]:
    #             # Check for anomaly
    #             if anomaly:
    #                 return anomaly

    #     # No Anomaly Found, continue at beginning
    #     for verticalSlice in self.Map:
    #         # Loop through anomalies
    #         for anomaly in verticalSlice:
    #             # Check for anomaly
    #             if anomaly:
    #                 return anomaly

    # def callLastAnomaly(self, currentPosition):
    #     # Set starting Slice
    #     startingSlice = currentPosition[1] + 1
    #     # Loop through Smaller Slices
    #     for verticalSlice in reversed(self.Map[:startingSlice]):
    #         # Set starting point
    #         startingPoint = currentPosition[0]
    #         # Loop through anomalies
    #         for anomaly in reversed(verticalSlice[:startingPoint]):
    #             # Check for anomaly
    #             if anomaly:
    #                 return anomaly

    #     # No Anomaly Found, continue at End
    #     for verticalSlice in reversed(self.Map):
    #         # Loop through anomalies
    #         for anomaly in reversed(verticalSlice):
    #             # Check for anomaly
    #             if anomaly:
    #                 return anomaly

    # def callAnomaly(self, Coordinates):
    #     verticalSlice = Coordinates[1]
    #     pointInSpace = Coordinates[0]

    #     anomaly = self.Map[verticalSlice][pointInSpace]

    #     return anomaly
