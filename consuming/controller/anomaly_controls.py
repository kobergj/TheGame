
def getAvailableSections(Anomaly, Player):
    """Checks for possible Actions with Anomaly"""
    sectionList = [Quit, Merchant, EquipmentDealer, Spaceport]

    availableSections = list()

    for possibleSection in sectionList:

        try:
            section = possibleSection(Anomaly, Player)

            availableSections.append(section)

        except AttributeError:
            pass

    return availableSections


# Anomaly Sections
class AnomalySection:
    """ Each Section of the Anomaly Contains the Interaction Information.
        Currently Implemented:
        Quit            - Quit Game

        Merchant        - Sells Goods
        EquipmentDealer - Sells Rooms

        Spaceport       - Depart from Anomaly
        """

    def __init__(self, Anomaly, Player):
        # Needs A Init Method which assigns all needed Stats

        # Interaction Type says what you can actualy DO with a Section
        self.interactionType = 'Nothing'
        # Main List object. For Example List of Goods, Rooms, Ships, etc..
        self.mainList = list()

    def __call__(self, Anomaly, Player, args=None):
        # Needs A Call Method which executes the Interaction
        return

    def __iter__(self):
        # For iteration
        return self

    def __len__(self):
        return len(self.mainList)

    def __getitem__(self, i):
        return self.mainList[i]

    def index(self, item):
        return self.mainList.index(item)

    def next(self):
        self.cursor += 1

        if self.cursor >= len(self.mainList):
            # Reset Cursor
            self.cursor = -1
            raise StopIteration

        item = self.mainList[self.cursor]

        return item, None

    def infoString(self):
        # Generate a Information String
        return 'None'



class Quit(AnomalySection):
    def __call__(self, Anomaly, Player, args=None):
        quit()

    def infoString(self):
        return 'Quit'


class Spaceport(AnomalySection):
    def infoString(self):
        return 'Spaceport - Depart'


class Merchant(AnomalySection):

    def __init__(self, Anomaly, Player):
        self.mainList = Anomaly.goodsProduced

        self.prices = Anomaly.prices

        self.interactionType = 'Buy'

        self.cursor = -1

    def __call__(self, Anomaly, Player, GoodToBuy):

        if not GoodToBuy:
            return

        # Currently One Good per buy
        Amount = 1

        price = self.prices[GoodToBuy]

        Player.spendCredits(price)

        Player.currentShip.loadCargo(GoodToBuy, Amount)

        return GoodToBuy

    def next(self):
        self.cursor += 1

        if self.cursor >= len(self.mainList):
            # Reset Cursor
            self.cursor = -1
            raise StopIteration

        good = self.mainList[self.cursor]

        price = self.prices[good]

        return good, price

    # I think this belongs to viz. Need a better Solution here
    def infoString(self):
        infoStr = ''

        infoStr += 'Merchant - Sells '

        for good in self.mainList:
            infoStr += '%s@%s ' % (good, self.prices[good])

        return infoStr

class EquipmentDealer(AnomalySection):
    def __init__(self, Anomaly, Player):
        self.mainList = Anomaly.roomsForSale

        self.interactionType = 'Buy'

        self.cursor = -1

    def __call__(self, Anomaly, Player, RoomToBuy):

        if not RoomToBuy:
            return

        Player.spendCredits(RoomToBuy.price)

        Player.currentShip.attachRoom(RoomToBuy)

    def index(self, roomName):
        for room in self.mainList:
            if room.name == roomName:
                break

        return self.mainList.index(room)

    def next(self):
        self.cursor += 1

        if self.cursor >= len(self.mainList):
            # Reset Cursor
            self.cursor = -1
            raise StopIteration

        room = self.mainList[self.cursor]

        price = room.price

        return room.name, price


    def infoString(self):
        infoStr = ''

        infoStr += 'Equipment Dealer - Sells Rooms'

        # for good in self.mainList:
        #     infoStr += '%s@%s ' % (good, self.prices[good])

        return infoStr
