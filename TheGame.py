import multiprocessing as mp

import configuration.database as db
import configuration.log_details as log

import controller.model_fabric as mf
import controller.viewmodel_fabric as vf

import view.basic_view as vwf


# TODO: Constants need to be configurable...
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

log.log('Initialize Queues')
viewmodel_queue = mp.Queue(maxsize=1)
choice_queue = mp.Queue(maxsize=1)

log.log('Initialize Model Producer')
modelProducer = mf.randomProducer(database, universe)

log.log('Initialize ViewModel Producer')
viewmodelProducer = vf.ViewModelProducer(universe, player, viewmodel_queue, choice_queue)

log.log('Craft Ship')
startingShip = mf.produceShip(database, STARTING_SHIP_STATS)

log.log('Board Ship')
player.switchShip(startingShip)

log.log('Set Starting Anomaly')
startingAnomaly = mf.produceAnomaly(database)
universe.addAnomaly(startingAnomaly)
player.travelTo(startingAnomaly.coordinates)


if __name__ == '__main__':
    log.log('Start Model Producer')
    modelProducer.startProducing()

    log.log('Fill Universe')
    universe.fill(NUMBER_OF_ANOMALIES)
    universe.update(player)

    log.log('Start ViewModel Producer')
    viewmodelProducer.startProducing()

    log.log('Init View')
    view = vwf.View(universe)

    # The Journey begins
    while True:
        # Get View Model
        view_model = viewmodel_queue.get()
        # Show View Model
        players_choice = view(view_model)
        # Returns Answer
        choice_queue.put(players_choice)

