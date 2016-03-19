
def getAvailableSections(Anomaly, Player):
    """Checks for possible Actions with Anomaly"""
    sectionList = [Quit, Merchant, Trader, EquipmentDealer, Gateport, Spaceport]

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
        Trader          - Buys Goods
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
        return 'Graveyard - Quit'


class Spaceport(AnomalySection):
    def infoString(self):
        return 'Spaceport - Depart'


class Merchant(AnomalySection):

    def __init__(self, Anomaly, Player):
        self.mainList = Anomaly.goodsProduced

        if Player.currentShip.cargoCapacity() <= 0:
            raise AttributeError

        self.prices = Anomaly.prices

        self.interactionType = 'Buy'

        self.cursor = -1

    def __call__(self, Anomaly, Player, GoodToBuy):

        if not GoodToBuy:
            return

        # Currently One Good per buy
        Amount = 1

        if Player.currentShip.cargoCapacity() <= 0:
            return

        Player.currentShip.loadCargo(GoodToBuy, Amount)

        price = self.prices[GoodToBuy]

        Player.spendCredits(price)

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

        infoStr += 'Merchant - Buy Goods Here'

        return infoStr


class Trader(AnomalySection):

    def __init__(self, Anomaly, Player):
        sharedGoods = set(Anomaly.goodsConsumed).intersection(set(Player.currentShip.inCargo.keys()))

        if not sharedGoods:
            raise AttributeError

        # Build Main List
        self.mainList = list(sharedGoods)

        self.prices = Anomaly.prices

        self.interactionType = 'Sell'

        self.cursor = -1

    def __call__(self, Anomaly, Player, GoodToSell):

        if not GoodToSell:
            return

        # Currently One Good per buy
        Amount = 1

        price = self.prices[GoodToSell]

        Player.earnCredits(price)

        Player.currentShip.unloadCargo(GoodToSell, Amount)

        return GoodToSell

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

        infoStr += 'Trader - Sell Goods Here'

        return infoStr

class EquipmentDealer(AnomalySection):
    def __init__(self, Anomaly, Player):
        self.mainList = Anomaly.roomsForSale

        if not Anomaly.roomsForSale:
            raise AttributeError

        self.interactionType = 'Buy'

        self.cursor = -1

    def __call__(self, Anomaly, Player, RoomToBuy):

        if not RoomToBuy:
            return

        Player.spendCredits(RoomToBuy.price)

        Player.currentShip.attachRoom(RoomToBuy)

        Anomaly.roomsForSale.remove(RoomToBuy)

        return True

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


class Gateport(AnomalySection):
    def __init__(self, Anomaly, Player):
        self.mainList = list()

        self.costForUse = Anomaly.costForUse

        self.interactionType = 'Travel'

        self.cursor = -1

    def __call__(self, Anomaly, Player):
        Player.spendCredits(self.costForUse)

        Player.currentShip.maxTravelDistance.mock(9999999)
        Player.currentShip.maintenanceCosts.mock(0.00000001)

    def infoString(self):
        infoStr = ''

        infoStr += 'Gate Port - Jump to Anywhere in Space'

        return infoStr
