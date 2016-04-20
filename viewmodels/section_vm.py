import configuration.log_details as log
import view_models.basic_vm as bvm

# Anomaly Sections
class AnomalySection(bvm.BasicViewModel):
    """ Each Section of the Anomaly Contains the Interaction Information.
        Currently Implemented:
        Quit            - Quit Game

        Merchant        - Sells Goods
        Trader          - Buys Goods
        EquipmentDealer - Sells Rooms

        Spaceport       - Depart from Anomaly
        """

    def __init__(self, Anomaly, Player, AnomalyViewModel):
        bvm.BasicViewModel.__init__(self, Anomaly, Player)

        # Interaction Type says what you can actualy DO with a Section
        self.interactionType = 'Nothing'

        self.parent = AnomalyViewModel

    def __call__(self, Anomaly, Player, *args):
        # Needs A Call Method which executes the Interaction
        pass

    def __iter__(self):
        # For iteration
        return iter([(lambda x: x[0])(x) for x in self.choice_list])

    def __len__(self):
        return len(self.choice_list)

    def __getitem__(self, i):
        return self.choice_list[i]

    def infoString(self):
        # Generate a Information String
        return 'None'

    # def index(self, item):
    #     return self.choice_list.index(item)

    # def next(self):
    #     self.cursor += 1

    #     if self.cursor >= len(self.mainList):
    #         # Reset Cursor
    #         self.cursor = -1
    #         raise StopIteration

    #     item = self.mainList[self.cursor]

    #     return item




class Quit(AnomalySection):
    def __call__(self, Anomaly, Player, *args):
        quit()

    def infoString(self):
        return 'Graveyard'


# class Spaceport(AnomalySection):
#     def __call__(self, Anomaly, Player, *args):
#         Player.depart()

#     def infoString(self):
#         return 'Spaceport'


class Merchant(AnomalySection):

    def __init__(self, Anomaly, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Anomaly, Player)

        self.interactionType = 'Buy'

        self.choice_list = Anomaly.goodsProduced

    def __call__(self):

        if not self.player_choice:
            return AnomalyViewModel

        GoodToBuy = self.choice_list[self.player_choice-1]

        # Currently One Good per buy
        Amount = 1

        self.player.currentShip.loadCargo(GoodToBuy, Amount)

        price = GoodToBuy.price

        self.player.spendCredits(price)

        if self.player.currentShip.cargoCapacity() > 0:
            return Merchant

        return AnomalyViewMode


    def infoString(self):
        return 'Merchant'


class Trader(AnomalySection):

    def __init__(self, Anomaly, Player):
        # Calculate Shared Goods:
        sharedGoods = list()

        for good in Anomaly.goodsConsumed:
            log.log('Checking for Similarities: %s - %s' % (good.name, Player.currentShip.inCargo.keys()))
            if good.name in Player.currentShip.inCargo:
                sharedGoods.append(good)
        # sharedGoods = set(Anomaly.goodsConsumed).intersection(set(Player.currentShip.inCargo.keys()))

        if not sharedGoods:
            raise AttributeError

        # Build Main List
        self.mainList = sharedGoods

        self.interactionType = 'Sell'

        self.cursor = -1

    def __call__(self, Anomaly, Player, GoodToSell):

        if not GoodToSell:
            return

        # Currently One Good per buy
        Amount = 1

        price = GoodToSell.price

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

        return good

    # I think this belongs to viz. Need a better Solution here
    def infoString(self):
        infoStr = ''

        infoStr += 'Trader'

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

        return room


    def infoString(self):
        infoStr = ''

        infoStr += 'Equipment Dealer'

        return infoStr


class Gateport(AnomalySection):
    def __init__(self, Anomaly, Player):
        self.mainList = list()

        self.costForUse = Anomaly.costForUse

        self.interactionType = 'Travel'

        self.cursor = -1

    def __call__(self, Anomaly, Player, *args):
        Player.spendCredits(self.costForUse)

        Player.currentShip.maxTravelDistance.mock(9999999)
        Player.currentShip.maintenanceCosts.mock(0.00000001)

    def infoString(self):
        infoStr = ''

        infoStr += 'Gate Port'

        return infoStr
