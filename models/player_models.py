import logging

log = logging.getLogger('model')


class Player():
    def __init__(self, playerInfo):
        # Player Name
        self.name = playerInfo['name']
        # Number Of Credits
        self.credits = playerInfo['startingCredits']
        # Ship
        self.currentShip = None
        # List of Old Ships
        self.deprecatedShips = list()
        # Current Postion
        self.currentPosition = None
        # Lets say you are alive at the beginning
        self.dead = False

    def land(self):
        self.atAnomaly = True

    def depart(self):
        self.atAnomaly = False

    def earnCredits(self, numberOfCredts):
        self.credits += numberOfCredts

    def spendCredits(self, numberOfCredts):
        self.credits -= numberOfCredts

    def switchShip(self, Ship):
        if self.currentShip:
            # load distance Dict
            Ship.distances = self.currentShip.distances
            # Scan Sector
            Ship.scanSector()
            # dump current Ship
            self.deprecatedShips.append(self.currentShip)

        # Attach Ship
        self.currentShip = Ship

    def travelTo(self, Coordinates):
        log.info('Player travelled to %s' % str(Coordinates))
        self.currentPosition = Coordinates
