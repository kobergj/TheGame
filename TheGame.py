import controller.planet_interactions as pi
import models.player as pyr
import models.universe as uvs
import generator.planets as gpl

NUMBER_OF_PLANETS = 5

player_info = {'name': 'Dr.Play', 'startingCredits': 12}
starting_ship_stats = {'cargoCapacity': 10, 'speed': 4}

# Initialize Player
player = pyr.Player(player_info, starting_ship_stats)

# generate List of Planets
listOfPlanets = gpl.generatePlanetList(NUMBER_OF_PLANETS)

# generate Anomaly Dict
anomalyInfos = {'planets': listOfPlanets}

# generate Universe
universe = uvs.Universe(anomalyInfos)

# Set starting Planet
next_destination_name = universe.planetList[0]

# Start
while next_destination_name != 'quit':
    planet = universe.__dict__[next_destination_name]

    next_destination_name = pi.Arrive(planet, player)
