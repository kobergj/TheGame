import controller.planet_interactions as pi
import models.player as pyr
import models.universe as uvs
import generator.planets as gpl

NUMBER_OF_PLANETS = 5

# Player Not yet Implemented
player_info = {'name': 'Dr.Play', 'startingCredits': 12}
player = pyr.Adventurer(player_info)

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
