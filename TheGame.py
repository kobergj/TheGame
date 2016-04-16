import consuming.model_consumer as con

import producing.model_producer as pro

import database.database as db

import logbook.configuration as log

NUMBER_OF_ANOMALIES = 25

MAX_COORDINATES = [15, 15]

PLAYER_INFO = {'name': 'Dr.Play',
               'startingCredits': 12
               }

STARTING_SHIP_STATS = {'cargoCapacity': 10,

                       'maintenanceCosts': 2,
                       'maxTravelDistance': 4,

                       'spaceForRooms': 2,

                       'price': 0,

                       'attackPower': 7,
                       'shieldStrength': 15,
                       }

# Init Log
log.initLogBook()

# Boot Database
database = db.DynamicDatabase

# Assign Player
player = pro.producePlayer(PLAYER_INFO)

# Generate Universe
universe = pro.produceUniverse(MAX_COORDINATES)

# Initialize Producer
randomProducer = pro.randomProducer(database, universe)

# Set Starting Anomaly
startingAnomaly = pro.produceAnomaly(database)

# Craft Ship
startingShip = pro.produceShip(database, STARTING_SHIP_STATS)

# Board Ship
player.switchShip(startingShip)

if __name__ == '__main__':
    # Start Producer
    randomProducer.startProducing()

    # Start Main Game
    journey = con.Journey(universe, player, startingAnomaly, NUMBER_OF_ANOMALIES)

    # The Journey ...
    while True:
        # continues
        journey(universe, player)
