import configuration.log_details as log
import viewmodels.basic_vm as bvm

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

    def __init__(self, Universe, Player, AnomalyViewModel):
        Anomaly = Universe[Player.currentPosition]

        bvm.BasicViewModel.__init__(self, Anomaly, Player)

        # Interaction Type says what you can actualy DO with a Section
        self.interactionType = 'Nothing'

        self.parent = AnomalyViewModel

        self.choice_list = [None]

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




# class Quit(AnomalySection):
#     def __call__(self, Anomaly, Player, *args):
#         quit()

#     def infoString(self):
#         return 'Graveyard'


# class Spaceport(AnomalySection):
#     def __call__(self, Anomaly, Player, *args):
#         Player.depart()

#     def infoString(self):
#         return 'Spaceport'


class Merchant(AnomalySection):

    def __init__(self, Universe, Player, AnomalyViewModel):

        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        self.interactionType = 'Buy'

        for good in Universe[Player.currentPosition].goodsProduced:
            self.choice_list.append(good)


    def __call__(self):

        if not self.player_choice:
            return self.parent

        GoodToBuy = self.choice_list[self.player_choice]

        # Currently One Good per buy
        Amount = 1

        self.player.currentShip.loadCargo(GoodToBuy, Amount)

        price = GoodToBuy.price

        self.player.spendCredits(price)

        if self.player.currentShip.cargoCapacity() > 0:
            return Merchant

        return self.parent


    def infoString(self):
        return 'Merchant'


class Trader(AnomalySection):

    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)
        # Calculate Shared Goods:
        sharedGoods = list()

        for good in Universe[Player.currentPosition].goodsConsumed:
            log.log('Checking for Similarities: %s - %s' % (good.name, Player.currentShip.inCargo.keys()))
            if good.name in Player.currentShip.inCargo:
                sharedGoods.append(good)

        # if not sharedGoods:
        #     raise AttributeError

        # Build Main List
        for good in sharedGoods:
            self.choice_list.append(good)

        self.interactionType = 'Sell'

    def __call__(self):

        if not self.player_choice:
            return self.parent

        GoodToSell = self.choice_list[self.player_choice]

        # Currently One Good per sell
        Amount = 1

        self.player.currentShip.unloadCargo(GoodToSell, Amount)

        price = GoodToSell.price

        self.player.earnCredits(price)

        return Trader

    def infoString(self):
        return 'Trader'

class EquipmentDealer(AnomalySection):
    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        for room in self.anomaly.roomsForSale:
            self.choice_list.append(room)

        self.interactionType = 'Buy'

    def __call__(self):

        if not self.player_choice:
            return self.parent

        RoomToBuy = self.choice_list[self.player_choice]

        self.player.spendCredits(RoomToBuy.price)

        self.player.currentShip.attachRoom(RoomToBuy)

        self.anomaly.roomsForSale.remove(RoomToBuy)

        return EquipmentDealer

    def infoString(self):
        return 'Equipment Dealer'


class Gateport(AnomalySection):
    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        self.interactionType = 'Travel'

        self.cost_for_use = self.anomaly.costForUse

    def __call__(self):
        self.player.spendCredits(self.cost_for_use)

        self.player.currentShip.maxTravelDistance.mock(9999999)
        self.player.currentShip.maintenanceCosts.mock(0.00000001)

        return self.parent

    def infoString(self):
        return 'Gate Port'
