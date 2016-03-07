
class Room():
    def __init__(self, roomInformation):
        self.name = roomInformation['name']

        self.price = roomInformation['price']

        self.statBoosts = roomInformation['statBoosts']

    def powerUp(self, Ship):
        for stat, boost in self.statBoosts:
            Ship.__dict__[stat] += boost

    def powerDown(self, Ship):
        for stat, boost in self.statBoosts:
            Ship.__dict__[stat] -= boost


class CargoBay(Room):
    def __init__(self, roomInformation):
        Room.__init__(roomInformation)
