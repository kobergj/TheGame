import controller.planet_interactions as pi
import models.player as pyr
import models.universe as uvs

player_info = {'name': 'Dr.Play', 'startingCredits': 12}

earth_info = {'name': 'Earth', 'goodsConsumed': ['Videogames'], 'goodsProduced': ['Gin'], 'coordinates': [0, 1, 0]}
mars_info = {'name': 'Mars', 'goodsProduced': ['Sand', 'Evil'], 'goodsConsumed': ['Gin'], 'coordinates': [0, 1, 0]}

anomalyInfos = {'planets': [earth_info, mars_info]}

universe = uvs.Universe(anomalyInfos)

player = pyr.Adventurer(player_info)

next_destination = pi.Arrive(universe.Earth, player)

while next_destination is not None:
    next_destination = pi.Arrive(universe.planetList[next_destination], player)
