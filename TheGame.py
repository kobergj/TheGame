import controller.planet_interactions as pi
import controller.universe_interactions as ui
import models.player as pyr
import models.universe as uvs
import generator.universe as guv

NUMBER_OF_PLANETS = 10

player_info = {'name': 'Dr.Play', 'startingCredits': 12}
starting_ship_stats = {'cargoCapacity': 10, 'speed': 4, 'maxTravelDistance': 10}

# Initialize Player
player = pyr.Player(player_info, starting_ship_stats)

# generate Universe Information
universeInfos = guv.generateUniverseInformation(NUMBER_OF_PLANETS)

# generate Universe
universe = uvs.Universe(universeInfos)

# Set starting Planet
next_destination_name = universe.planetList[0]

# Start
while next_destination_name != 'quit':
    planet = universe.__dict__[next_destination_name]

    player.currentShip.scanSector(planet.distances)

    next_destination_name = pi.Arrive(planet, player)

    if not next_destination_name:
        next_destination_name = ui.ChooseDestination(universe, player)
