import math

import viewmodels.basic_vm as bvm
import viewmodels.anomaly_vm as avm

import configuration.log_details as log

class UniverseViewModel(bvm.BasicViewModel):

    scan_index = 0
    update = False

    def __init__(self, universe, player, update):

        self.available_anomalies = self.get_available_anomalies(universe, player)

        bvm.BasicViewModel.__init__(self, self.available_anomalies[self.scan_index], player)

        self.choice_list = [True, False]

        self.parent = update

        if self.parent:
            log.log('Update Universe')
            universe.update(player)

    def __call__(self):
        choice = self.choice_list[self.player_choice]

        if choice:
            log.log('Execute Travel Logic')
            land = self.Travel(self.anomaly, self.player)

            if land:
                self.parent = UniverseViewModel
                return avm.AnomalyViewModel

            UniverseViewModel.scan_index = 0
            self.parent = True
            return UniverseViewModel

        UniverseViewModel.scan_index += 1
        if UniverseViewModel.scan_index >= len(self.available_anomalies):
            UniverseViewModel.scan_index = 0

        self.parent = False
        return UniverseViewModel

    def Travel(self, Anomaly, Player):
        """Player travels to Anomaly."""

        # Is current?
        if Anomaly.coordinates == Player.currentPosition:
            log.log('%(name)s is current. Landing...' % Anomaly.__dict__)
            Player.land()
            return True

        log.log('Pay Costs of %(travelCosts)s' % Anomaly.__dict__)
        Player.spendCredits(Anomaly.travelCosts)
        log.log('Traveling to %(name)s' % Anomaly.__dict__)
        Player.travelTo(Anomaly.coordinates)

        # Demock Stats
        Player.currentShip.maxTravelDistance.demock()
        Player.currentShip.maintenanceCosts.demock()


    def get_available_anomalies(self, universe, player):

        dist_calc = DistanceCalculator(player.currentPosition)

        distance_list=list()
        for anomaly in universe:
            distance_list.append([anomaly, dist_calc(anomaly.coordinates)])

        distance_list.sort(key=(lambda x: x[1]))

        available_anomalies = list()

        while len(available_anomalies) < player.currentShip.maxTravelDistance():
            try:
                available_anomalies.append(distance_list.pop(0)[0])
            except IndexError:
                return available_anomalies

        return available_anomalies

    def calculateTravelCosts(self, Player, Distance):
        # Check if reachable
        if Distance <= Player.currentShip.maxTravelDistance():
            # Calculate Costs
            travelCosts = int(Distance * Player.currentShip.maintenanceCosts())

            return travelCosts

        return None


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


