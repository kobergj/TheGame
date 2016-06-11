import math

import basic_vm as bvm
import anomaly_vm as avm
import fight_vm as fvm

import logging

import controller.model_operations as mo

log = logging.getLogger('viewmodel')

class UniverseViewModel(bvm.BasicViewModel):

    scan_index = 0

    def __init__(self, universe, player, *args):

        self.anomaly_availability = self.get_available_anomalies(universe, player)

        anomaly = self.anomaly_availability[0][self.scan_index]

        bvm.BasicViewModel.__init__(self, anomaly, player, UniverseViewModel)

    def __call__(self, universe, player):
        if self.player_choice == 0:
            anomaly = universe[self.anomaly.coordinates]

            self.Travel(anomaly, player)
            universe.request_update = True

    def next(self, player_choice):
        choice = self.choice_list[player_choice]

        if choice:
            UniverseViewModel.scan_index = 0
            self.player_choice = 0

            if self.anomaly.enemies:
                return fvm.FightViewModel

            if self.anomaly.coordinates == self.player.currentPosition:
                self.player_choice = 1
                return avm.AnomalyViewModel

            return UniverseViewModel

        UniverseViewModel.scan_index += 1
        if UniverseViewModel.scan_index >= len(self.anomaly_availability[0]):
            UniverseViewModel.scan_index = 0

        self.player_choice = 2
        return UniverseViewModel

    def Travel(self, Anomaly, Player):
        """Player travels to Anomaly."""
        # Is current?
        dist_calc = DistanceCalculator(Player.currentPosition)
        distance = dist_calc(Anomaly.coordinates)
        costs = self.calculateTravelCosts(Player, distance)

        log.info('Pay Costs of %(travelCosts)s' % Anomaly.__dict__)
        Player.spendCredits(costs)
        log.info('Traveling to %(name)s' % Anomaly.__dict__)
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


