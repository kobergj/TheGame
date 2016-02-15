
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

    def earnCredits(self, numberOfCredts):
        self.credits += numberOfCredts

    def spendCredits(self, numberOfCredts):
        self.credits -= numberOfCredts

    def switchShip(self, Ship):
        if self.currentShip:
            self.deprecatedShips.append(self.currentShip)

        self.currentShip = Ship
