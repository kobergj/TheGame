import controller.anomaly_interactions as ai

import models.player as pyr
import models.universe as uvs
import models.ships as shp

import generator.producer as gpr

import database.database as db

import threading

NUMBER_OF_ANOMALIES = 18

MIN_COORDINATES = [0, 0]
MAX_COORDINATES = [20, 20]

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

# generate Universe
universe = uvs.Universe(MIN_COORDINATES, MAX_COORDINATES)

# get Database
database = db.DynamicDatabase

# Create Producer Thread
producerThread = threading.Thread(target=gpr.Producer, args=(database, universe))
# Make Him a Daemon
producerThread.daemon = True
# Give Him a Name
producerThread.name = 'ProducerThread'
# Start Producer
producerThread.start()

# Fill Universe
while len(universe.anomalyList) < NUMBER_OF_ANOMALIES:
    anomaly = universe.anomalyQ.get()

    universe.addAnomaly(anomaly)

# Set starting Anomaly
startingAnomaly = universe.anomalyList.keys()[0]

# Travel to Starting Planet
player.travelTo(startingAnomaly)

if __name__ == '__main__':
    # Start
    while True:
        ai.Arrive(player, universe)
