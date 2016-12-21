import logging

import basic_vm as bvm
import controller.model_operations as mo

log = logging.getLogger('viewmodel')

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

        bvm.BasicViewModel.__init__(self, Anomaly, Player, AnomalyViewModel)

        # Interaction Type says what you can actualy DO with a Section
        self.interactionType = 'Nothing'

        self.choice_list = [None]

    def __iter__(self):
        # For iteration
        return iter([(lambda x: x[0])(x) for x in self.choice_list])

    def __len__(self):
        return len(self.choice_list)

    def __getitem__(self, i):
        return self.choice_list[i]

    def next(self, player_choice):
        self.player_choice = player_choice
        # Returns next view model
        return self.parent

    def infoString(self):
        # Generate a Information String
        return 'None'

class Merchant(AnomalySection):

    def __init__(self, Universe, Player, AnomalyViewModel):

        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        self.interactionType = 'Buy'

        mrch = Universe[Player.currentPosition].merchant

        for good in mrch.show_stock():
            cargobay = Player.currentShip.access_content('cargobay')

            if not cargobay.full():
                self.choice_list.append(good)

    def __call__(self, player_choice):
        if not player_choice:
            return self.parent, mo.Pass()

        cargobay = self.player.currentShip.access_content('cargobay')

        if cargobay.free_space > 1:
            return Merchant, mo.BuyGood(self.choice_list[player_choice])

        return self.parent, mo.BuyGood(self.choice_list[player_choice])

    def infoString(self):
        return 'Merchant'

class Trader(AnomalySection):

    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)
        # Calculate Shared Goods:
        # sharedGoods = list()

        mrch = Universe[Player.currentPosition].merchant

        cargobay = self.player.currentShip.access_content('cargobay')

        for good in mrch.show_stock():
            # log.info('Checking for Similarities: %s - %s' % (good.name, Player.currentShip.inCargo.keys()))
            # if good.name in Player.currentShip.inCargo:
            #     sharedGoods.append(good)
            if good in cargobay:
                self.choice_list.append(good)


        # if not sharedGoods:
        #     raise AttributeError

        # Build Main List
        # for good in sharedGoods:
        #     self.choice_list.append(good)

        self.interactionType = 'Sell'

    def __call__(self, player_choice):
        # self.player_choice = player_choice

        if not player_choice:
            return self.parent, mo.Pass()

        return Trader, mo.SellGood(self.choice_list[player_choice])

    def infoString(self):
        return 'Trader'

class EquipmentDealer(AnomalySection):
    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        for room in self.anomaly.roomsForSale:
            self.choice_list.append(room)

        self.interactionType = 'Buy'

    def __call__(self, universe, player):
        if not self.player_choice:
            return

        RoomToBuy = self.choice_list[self.player_choice]

        player.spendCredits(RoomToBuy.price)

        player.currentShip.attachRoom(RoomToBuy)

        anomaly = universe[player.currentPosition]

        anomaly.remove_room(RoomToBuy)

        return


    def next(self, player_choice):
        self.player_choice = player_choice

        if not player_choice:
            return self.parent

        return EquipmentDealer

    def infoString(self):
        return 'Equipment Dealer'


class Gateport(AnomalySection):
    def __init__(self, Universe, Player, AnomalyViewModel):
        AnomalySection.__init__(self, Universe, Player, AnomalyViewModel)

        self.interactionType = 'Travel'

        self.jumpgate = self.anomaly.jumpgate

    def __call__(self, player_choice):
        if not player_choice:
            return self.parent, mo.Pass()

        return self.parent, mo.EnterJumpgate(self.jumpgate.show_price())

    # def infoString(self):
    #     return 'Gate Port'
