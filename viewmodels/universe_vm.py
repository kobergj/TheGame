import math

import viewmodels.basic_vm as bvm
import viewmodels.anomaly_vm as avm

import logging

class UniverseViewModel(bvm.BasicViewModel):

    scan_index = 0
    update = False

    def __init__(self, universe, player, update):

        self.anomaly_availability = self.get_available_anomalies(universe, player)

        available_anomalies = self.anomaly_availability[0]

        bvm.BasicViewModel.__init__(self, available_anomalies[self.scan_index], player)

        self.choice_list = [True, False]

        self.parent = update

        # if self.parent:
        #     logging.info('Update Universe')
        #     universe.update(player)

    def __call__(self, universe, player):
        if self.player_choice == 0:
            anomaly = universe[self.anomaly.coordinates]

            self.Travel(anomaly, player)

            universe.request_update = True

        # if self.player_choice == 1:
        #     player.land()

        return

    def next(self, player_choice):
        choice = self.choice_list[player_choice]

        if choice:
            if self.anomaly.coordinates == self.player.currentPosition:
                self.parent = UniverseViewModel
                self.player_choice = 1
                return avm.AnomalyViewModel

            UniverseViewModel.scan_index = 0
            self.parent = True
            self.player_choice = 0
            return UniverseViewModel

        UniverseViewModel.scan_index += 1
        if UniverseViewModel.scan_index >= len(self.anomaly_availability[0]):
            UniverseViewModel.scan_index = 0

        self.parent = False
        self.player_choice = 2
        return UniverseViewModel

    def Travel(self, Anomaly, Player):
        """Player travels to Anomaly."""
        # Is current?
        dist_calc = DistanceCalculator(Player.currentPosition)
        distance = dist_calc(Anomaly.coordinates)
        costs = self.calculateTravelCosts(Player, distance)

        logging.info('Pay Costs of %(travelCosts)s' % Anomaly.__dict__)
        Player.spendCredits(costs)
        logging.info('Traveling to %(name)s' % Anomaly.__dict__)
        Player.travelTo(Anomaly.coordinates)

    def get_available_anomalies(self, universe, player):

        dist_calc = DistanceCalculator(player.currentPosition)

        distance_list=list()
        for anomaly in universe:
            distance_list.append([anomaly, dist_calc(anomaly.coordinates)])

        distance_list.sort(key=(lambda x: x[1]))

        available_anomalies = list()
        not_available_anomalies = list()

        while len(available_anomalies) < player.currentShip.maxTravelDistance():
            try:
                anomaly, distance = distance_list.pop(0)
                available_anomalies.append(anomaly)
                anomaly.setTravelCosts(self.calculateTravelCosts(player, distance))

            except IndexError:
                return available_anomalies, not_available_anomalies

        while distance_list:
            not_available_anomalies.append(distance_list.pop(0)[0])

        return available_anomalies, not_available_anomalies

    def calculateTravelCosts(self, Player, Distance):
        # Calculate Costs
        travelCosts = int(Distance * Player.currentShip.maintenanceCosts())

        return travelCosts


class DistanceCalculator:

    def __init__(self, position):
        self.position = position

    def __call__(self, coordinates):
        distance = 0.0
        for i in range(len(coordinates)):
            x = coordinates[i]
            y = self.position[i]

            distance += (x - y)**2

        distance = math.sqrt(distance)
        distance = round(distance, 2)

        return distance

