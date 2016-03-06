import controller.anomaly_interactions as ai

import models.player as pyr
import models.universe as uvs
import models.ships as shp

import generator.producer as gpr

import database.database as db

import threading

NUMBER_OF_ANOMALIES = 20

MIN_COORDINATES = [0, 0]
MAX_COORDINATES = [10, 10]

PLAYER_INFO = {'name': 'Dr.Play',
               'startingCredits': 12
               }

STARTING_SHIP_STATS = {'cargoCapacity': 10,

                       'speed': 2,
                       'maxTravelDistance': 4,

                       'spaceForRooms': 2,

                       'price': 0,

                       'attackPower': 22,
                       'shieldStrength': 10,
                       }

# Initialize Player
player = pyr.Player(PLAYER_INFO)

# Initialize Ship
startingShip = shp.Ship(STARTING_SHIP_STATS)

# generate Universe
universe = uvs.Universe(MIN_COORDINATES, MAX_COORDINATES)

# get Database
database = db.DynamicDatabase()

# Create Producer Thread
producerThread = threading.Thread(name='ProducerThread', target=gpr.Producer, args=(database, universe))
# Make Him a Daemon
producerThread.daemon = True
# Start Producer
producerThread.start()

# Fill Universe
while len(universe.anomalyList) < NUMBER_OF_ANOMALIES:
    # Get Anomaly
    anomaly = universe.anomalyQ.get()
    # Add Anomaly
    universe.addAnomaly(anomaly)

# Set starting Anomaly
startingAnomaly = universe.anomalyList.keys()[0]

# Board Ship
player.switchShip(startingShip)

# Travel to Starting Anomaly
player.travelTo(startingAnomaly)

if __name__ == '__main__':
    # Start
    while True:
        # Arrive at Anomaly
        ai.Arrive(player, universe)
