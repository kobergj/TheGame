
class Room():
    def __init__(self, roomInformation):
        self.name = roomInformation['name']
        self.statBoosts = roomInformation['statBoosts']

    def attachAt(self, Ship):
        for stat in self.statBoosts:
            Ship.__dict__[stat] += stat

    def detachFrom(self, Ship):
        for stat in self.statBoosts:
            Ship.__dict__[stat] -= stat
