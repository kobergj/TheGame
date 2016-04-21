import configuration.database as db
import configuration.log_details as log

import controller.model_fabric as mf

import view.basic_view as vwf

import viewmodels.universe_vm as uvm

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

log.log('Init Database')
database = db.DynamicDatabase

log.log('Assigning Player')
player = mf.producePlayer(PLAYER_INFO)

log.log('Generate Universe')
universe = mf.produceUniverse(MAX_COORDINATES)

log.log('Initialize Producer')
randomProducer = mf.randomProducer(database, universe)

log.log('Craft Ship')
startingShip = mf.produceShip(database, STARTING_SHIP_STATS)

log.log('Board Ship')
player.switchShip(startingShip)

log.log('Set Starting Anomaly')
startingAnomaly = mf.produceAnomaly(database)
universe.addAnomaly(startingAnomaly)
player.travelTo(startingAnomaly.coordinates)


if __name__ == '__main__':
    log.log('Start Producer')
    randomProducer.startProducing()

    log.log('Fill Universe')
    universe.fill(NUMBER_OF_ANOMALIES)
    universe.update(player)

    log.log('Init View')
    view = vwf.View(universe)

    # Set Starting ViewModel
    view_model_class = uvm.UniverseViewModel

    # The Journey ...
    while True:
        view_model = view_model_class(universe, player)

        view(view_model)

        view_model_class = view_model()



