import controller.viewmodel_fabric as vf
import controller.model_fabric as mf

import configuration.database as db
import configuration.log_details as log

import models.game_models as gm

import view.basic_view as vwf

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

# Init Game 
game = gm.RandomGame(PLAYER_INFO, MAX_COORDINATES, STARTING_SHIP_STATS, NUMBER_OF_ANOMALIES)


if __name__ == '__main__':
    # Start Producer
    game.randomProducer.startProducing()

    # Init View
    view = vwf.View()

    # The Journey ...
    while True:
        # I guess it should look like this
        view_model = game()

        view(view_model)

        view_model()
