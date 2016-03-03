
class Room():
    def __init__(self, roomInformation):
        self.name = roomInformation['name']

        self.price = roomInformation['price']

    def powerUp(self, Ship):
        pass

    def powerDown(self, Ship):
        pass


class CargoBay(Room):
    def __init__(self, roomInformation):
        Room.__init__(roomInformation)
