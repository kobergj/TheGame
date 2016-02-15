import controller.planet_interactions as pi
import controller.universe_interactions as ui
import controller.spacegate_interactions as sgi
import controller.starbase_interactions as sbi

import models.player as pyr
import models.universe as uvs
import models.ships as shp

import generator.universe as guv

NUMBER_OF_PLANETS = 10
NUMBER_OF_SPACEGATES = 3
NUMBER_OF_STARBASES = 3

player_info = {'name': 'Dr.Play', 'startingCredits': 12}
starting_ship_stats = {'cargoCapacity': 10, 'speed': 2, 'maxTravelDistance': 4, 'spaceForRooms': 2}

# Initialize Player
player = pyr.Player(player_info)

# Initialize Ship
startingShip = shp.Ship(starting_ship_stats)

# Board Ship
player.switchShip(startingShip)

# generate Universe Information
universeInfos = guv.generateUniverseInformation(NUMBER_OF_PLANETS,
                                                NUMBER_OF_SPACEGATES,
                                                NUMBER_OF_STARBASES
                                                )

# generate Universe
universe = uvs.Universe(universeInfos)

# Set starting Planet
next_destination_name = universeInfos['anomalyInformations']['Planet'][0]['name']

# Start
while True:
    # Get Anomaly
    anomaly = universe.anomalyList[next_destination_name]

    # scan Sector
    universe.updateDistances(player.currentShip, anomaly.coordinates)
    player.currentShip.scanSector()

    # Choose Next Destination
    next_destination_name = ui.ChooseDestination(universe, player)

    # Solution Suboptimal
    while next_destination_name == 'land':
        if anomaly.__class__.__name__ == 'Planet':
            # Arrive at Planet
            pi.Arrive(anomaly, player)

        elif anomaly.__class__.__name__ == 'Spacegate':
            # Arrive at Spacegate
            sgi.Arrive(anomaly, player)

        elif anomaly.__class__.__name__ == 'Starbase':
            # Arrive at Starbase
            sbi.Arrive(anomaly, player)

        # Choose Next Destination
        next_destination_name = ui.ChooseDestination(universe, player)
