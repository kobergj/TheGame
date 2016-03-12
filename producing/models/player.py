
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
        self.currentPosition = Coordinates
