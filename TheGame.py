import multiprocessing as mp
from datetime import datetime as dt

import configuration.database as db
import configuration.log_details as log

import controller.model_fabric as mf
import controller.viewmodel_fabric as vf

import view.basic_view as vwf

# Starting Time Stamp
start = dt.now()

# Init Log
log.initLogBook()

log.log('Init Database')
database = db.DynamicDatabase

log.log('Creating Connections')
model_connection = mp.Pipe()
view_connection = mp.Pipe()

log.log('Initialize Model Producer')
modelProducer = mf.randomProducer(database, model_connection[0])

log.log('Initialize ViewModel Producer')
viewmodelProducer = vf.ViewModelProducer(model_connection[1], view_connection[0])

log.log('Init View')
view = vwf.View(database)

if __name__ == '__main__':
    log.log('Start Model Producer')
    modelProducer.startProducing()

    log.log('Start ViewModel Producer')
    viewmodelProducer.startProducing()

    # May be "True" is not the best option...
    while True:
        # Get View Model
        view_model = view_connection[1].recv()
        # Show View Model
        players_choice = view(view_model)
        # Lame
        if players_choice == 'I wanna quit the goddamn Game!':
            break
        # Return Answer
        view_connection[1].send(players_choice)


    # Clean Up
    modelProducer.stopProducing()
    viewmodelProducer.stopProducing()
    view_connection[1].close()
    model_connection[1].close()
    log.log('Done. Session %s' % (dt.now() - start))