import models.anomalies as anm
import controller.planet_interactions as pi


earth_info = {'name': 'Earth', 'goodsConsumed': ['Videogames'], 'goodsProduced': ['Gin']}
mars_info = {'name': 'Mars', 'goodsProduced': ['Sand', 'Evil'], 'goodsConsumed': ['Gin']}

Earth = anm.Planet(earth_info)
Mars = anm.Planet(mars_info)

Planets = [Earth, Mars]

next_destination = pi.Arrive(Earth)

while next_destination is not None:
    next_destination = pi.Arrive(Planets[next_destination])
