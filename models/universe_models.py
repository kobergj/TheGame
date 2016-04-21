import Queue
import random
import configuration.log_details as log
import math

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
        self.coCursor = [-1, 0]

        return self

    def __getitem__(self, coordinates):
        vSlice = coordinates[1]
        point = coordinates[0]

        return self.Map[vSlice][point]

    def next(self, infinity=False, start=None):
        # Init
        anomaly = None

        if start:
            self.coCursor = start

        # Start Loop
        while not anomaly:
            # Raise Point value of Cursor
            self.coCursor[0] += 1
            # Ran out of points?
            if self.coCursor[0] >= len(self.Map[0]):
                # Reset
                self.coCursor[0] = 0
                # Raise Slice Value of Cursor
                self.coCursor[1] += 1

            # Ran out of Slices?
            if self.coCursor[1] >= len(self.Map):

                if not infinity:
                    # Reset Cursor
                    self.coCursor = [-1, 0]
                    # Stop Iteration
                    raise StopIteration

                # Reset Cursor to Start
                self.coCursor = [0, 0]

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
        log.log('Assigned Coordinates %(name)s: %(coordinates)s' % Anomaly.__dict__)

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

    def update(self, Player):
        for anomaly in self:
            # Get Enemy from Queue
            newEnemy = self.enemyQ.get()
            # Append to Enemy List
            if newEnemy:
                anomaly.enemies.append(newEnemy)

            # Calculate Travel Costs
            distance = self.calculateDistance(Player.currentPosition, anomaly.coordinates)
            costs = self.calculateTravelCosts(Player, distance)
            log.log('Assigning TravelCosts %s to %s (dist: %s)' % (costs, anomaly.coordinates, distance))
            anomaly.setTravelCosts(costs)

            try:
                # Get Ship
                ship = self.shipQ.get()

                # Attach Ship to Station
                anomaly.changeShipForSale(ship)
            except AttributeError:
                pass

            try:
                # Delete One Room
                if anomaly.roomsForSale:
                    anomaly.roomsForSale.pop(0)

                # Fill Room List
                while len(anomaly.roomsForSale) < anomaly.maxRoomsForSale:
                    # Get Room
                    room = self.roomQ.get()

                    # Add Room
                    anomaly.addRoomForSale(room)
            except AttributeError:
                pass

    def calculateDistance(self, point1, point2):
        distance = 0.0
        for i in range(len(point1)):
            x = point1[i]
            y = point2[i]

            distance += (x - y)**2

        distance = math.sqrt(distance)
        distance = round(distance, 2)

        return distance

    def calculateTravelCosts(self, Player, Distance):
        # Calculate Costs
        travelCosts = int(Distance * Player.currentShip.maintenanceCosts())

        return travelCosts

    def fill(self, NumberOfAnomalies):
        for i in range(NumberOfAnomalies):
            # Get Anomaly
            anomaly = self.anomalyQ.get()
            # Add Anomaly
            self.addAnomaly(anomaly)

