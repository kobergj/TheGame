import controller.universe_interactions as ui
import controller.anomaly_interactions as ai

import models.player as pyr
import models.universe as uvs
import models.ships as shp

import generator.universe as guv
import generator.producer as gpr

import threading

NUMBER_OF_PLANETS = 10
NUMBER_OF_SPACEGATES = 4
NUMBER_OF_STARBASES = 5

player_info = {'name': 'Dr.Play',
               'startingCredits': 12
               }

starting_ship_stats = {'cargoCapacity': 10,
                       'speed': 2,
                       'maxTravelDistance': 4,
                       'spaceForRooms': 2,
                       'price': 0,
                       'attackPower': 4,
                       'shieldStrength': 10,
                       }

# Initialize Player
player = pyr.Player(player_info)

# Initialize switchShip
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

# Create Producer Thread
producerThread = threading.Thread(target=gpr.Producer, args=(universe, ))
producerThread.daemon = True
producerThread.name = 'ProducerThread'

# Start Producer
producerThread.start()

# Set starting Planet
startingPlanet = universeInfos['anomalyInformations']['Planet'][0]['name']
print startingPlanet
player.travelTo(startingPlanet)

if __name__ == '__main__':
    # Start
    while True:
        ai.Arrive(player, universe)
