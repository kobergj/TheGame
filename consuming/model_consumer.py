import consuming.controller.planet_interactions as pi
import consuming.controller.spacegate_interactions as sgi
import consuming.controller.starbase_interactions as sbi
import consuming.controller.enemy_interactions as emy
import consuming.controller.universe_interactions as ui

LOCATION_OF_ARRIVING_FUNCS = {
    'Planet': pi.Arrive,
    'Starbase': sbi.Arrive,
    'Spacegate': sgi.Arrive,
}


def fillUniverse(Universe, NumberOfAnomalies):

    for i in range(NumberOfAnomalies):
        # Get Anomaly
        anomaly = Universe.anomalyQ.get()
        # Add Anomaly
        Universe.addAnomaly(anomaly)


def interactWithAnomaly(Player, Universe):
    # Get Anomaly
    anomaly = Universe[Player.currentPosition]
    # Update Anomaly
    anomaly.update(Universe)

    # Choose Next Destination
    landAtAnomaly = ui.chooseInteractionType(Universe, Player)

    # Begin Landing Sequence
    while landAtAnomaly:
        # Fight ALL Enemies First
        while anomaly.enemies:
            # Get Enemy
            enemy = anomaly.enemies[0]
            # Begin Fight
            won = emy.beginFight(Player.currentShip, enemy)
            # Check For Winner
            if won:
                # Kill Enemy
                anomaly.enemies.remove(enemy)
            # Still a chance to flee
            landAtAnomaly = ui.chooseInteractionType(Universe, Player)
            # Check For Landing Sequence
            if not landAtAnomaly:
                return

        # Get Anomaly Class
        anomalyClass = anomaly.__class__.__name__
        # Get Arriving Func
        arrive = LOCATION_OF_ARRIVING_FUNCS[anomalyClass]
        # Arrive
        arrive(anomaly, Player)
        # Done Shopping?
        landAtAnomaly = ui.chooseInteractionType(Universe, Player)

    # def scanSector(self, distances):
    #     # init travelCost Dict
    #     travelCostDict = dict()
    #     nearestDestination = None

    #     # Loop through Destinations
    #     for destination, distance in distances.iteritems():
    #         travelCost = None
    #         # Check if in Travel Distance
    #         if distance <= self.maxTravelDistance:
    #             # Calculate Costs
    #             travelCost = int(distance * self.maintenanceCosts)

    #         # Update Dict
    #         travelCostDict.update({destination: travelCost})

    #         # update nearest - There is surely a better way for this
    #         if not nearestDestination:
    #             nearestDestination = destination

    #         elif distance <= distances[nearestDestination]:
    #             if distance != 0.0:
    #                 nearestDestination = destination

    #     # Check For Reachable Destinations
    #     if len(travelCostDict) < 2:
    #             travelCost = int(distances[nearestDestination] * self.maintenanceCosts)
    #             travelCostDict.update({nearestDestination: travelCost})

    #     # update travelCosts
    #     self.travelCosts = travelCostDict

    # def generateDistanceDict(self, currentCoordinates):
    #     # Init Distance Dict
    #     distances = dict()
    #     # Loop through Slices
    #     for verticalSlice in self.Map:
    #         # Loop through Anomalies
    #         for anomaly in verticalSlice:
    #             if anomaly:
    #                 # Calculate Distance
    #                 distance = self.calculateDistance(currentCoordinates, anomaly.coordinates)
    #                 # Update Distance Dist
    #                 distances.update({anomaly.name: distance})

    #     return distances
