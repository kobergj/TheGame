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
        self.distance_calculator = DistanceCalculator(player.currentPosition)

        self.anomaly_availability = self.get_available_anomalies(universe, player)

        anomaly = self.anomaly_availability[0][self.scan_index]

        bvm.BasicViewModel.__init__(self, anomaly, player, UniverseViewModel)

    def D__call__(self, universe, player):
        if self.player_choice == 0:
            anomaly = universe[self.anomaly.coordinates]

            self.Travel(anomaly, player)
            universe.request_update = True

    def __call__(self, player_choice):
        choice = self.choice_list[player_choice]

        if choice:
            UniverseViewModel.scan_index = 0
            self.player_choice = 0

            cords = self.anomaly.coordinates
            dstc = self.distance_calculator(self.anomaly.coordinates)

            if self.anomaly.enemies:
                return fvm.FightViewModel, mo.Travel(cords, dstc)

            if self.anomaly.coordinates == self.player.currentPosition:
                self.player_choice = 1
                return avm.AnomalyViewModel, mo.Pass()

            return UniverseViewModel, mo.Travel(cords, dstc)

        UniverseViewModel.scan_index += 1
        if UniverseViewModel.scan_index >= len(self.anomaly_availability[0]):
            UniverseViewModel.scan_index = 0

        self.player_choice = 2
        return UniverseViewModel, mo.Pass()

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

        distance_list=list()
        for anomaly in universe:
            distance_list.append([anomaly, self.distance_calculator(anomaly.coordinates)])

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


