import models.ships as shp


class Player():
    def __init__(self, playerInfo, startingShipStats):
        self.name = playerInfo['name']
        self.credits = playerInfo['startingCredits']

        self.currentShip = shp.Ship(startingShipStats)

    def earnCredits(self, numberOfCredts):
        self.credits += numberOfCredts

    def spendCredits(self, numberOfCredts):
        self.credits -= numberOfCredts
