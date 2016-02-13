import controller.planet_interactions as pi
import controller.universe_interactions as ui
import controller.spacegate_interactions as sgi
import models.player as pyr
import models.universe as uvs
import generator.universe as guv

NUMBER_OF_PLANETS = 10
NUMBER_OF_SPACEGATES = 3

player_info = {'name': 'Dr.Play', 'startingCredits': 12}
starting_ship_stats = {'cargoCapacity': 10, 'speed': 2, 'maxTravelDistance': 8}

# Initialize Player
player = pyr.Player(player_info, starting_ship_stats)

# generate Universe Information
universeInfos = guv.generateUniverseInformation(NUMBER_OF_PLANETS, NUMBER_OF_SPACEGATES)

# generate Universe
universe = uvs.Universe(universeInfos)

# Set starting Planet
next_destination_name = universe.planetList[0]

# Start
while True:
    # Get Anomaly
    anomaly = universe.__dict__[next_destination_name]

    # scan Sector
    player.currentShip.scanSector(anomaly.distances)

    # Solution Suboptimal
    if anomaly.name in universe.planetList:
        # Arrive at Planet
        pi.Arrive(anomaly, player)

    elif anomaly.name in universe.spacegateList:
        # Arrive at Spacegate
        sgi.Arrive(anomaly, player)

    next_destination_name = ui.ChooseDestination(universe, player)
