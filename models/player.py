class Adventurer():
    def __init__(self, playerInfo):
        self.name = playerInfo['name']
        self.credits = playerInfo['startingCredits']

    def earnCredits(self, numberOfCredts):
        self.credits -= numberOfCredts

    def spendCredits(self, numberOfCredts):
        self.credits -= numberOfCredts
