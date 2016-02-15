
class Room():
    def __init__(self, roomInformation):
        self.name = roomInformation['name']
        self.statBoosts = roomInformation['statBoosts']

    def powerUp(self, Ship):
        for stat in self.statBoosts:
            Ship.stats[stat] += stat

    def powerDown(self, Ship):
        for stat in self.statBoosts:
            Ship.stats[stat] -= stat
