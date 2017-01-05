import multiprocessing as mp
from datetime import datetime as dt
import logging

import logbook.log_configuration # Singleton via Import

import database.main_database as db

import controller.model_fabric_new as mf
import controller.viewmodel_fabric as vf

import view.basic_view as vwf

# Starting Time Stamp
start = dt.now()

# Init Database
database = db.Database

# main thread logger
log = logging.getLogger('view')

log.critical('Starting -- %s' % start)

log.info('Creating Connections')
model_connection = mp.Pipe()
view_connection = mp.Pipe()

log.info('Initialize Model Producer')
modelProducer = mf.ModelHandler(database, model_connection[0])

log.info('Initialize ViewModel Producer')
viewmodelProducer = vf.ViewModelProducer(model_connection[1], view_connection[0])

log.info('Init View')
view = vwf.View(database)

if __name__ == '__main__':
    log.info('Start Model Producer')
    modelProducer.start()

    log.info('Start ViewModel Producer')
    viewmodelProducer.startProducing()

    players_choice = True

    while players_choice is not None:
        log.info('Get View Model')
        view_model = view_connection[1].recv()
        log.info('Show View Model')
        players_choice = view(view_model)
        log.info('Sending %s' % players_choice)
        view_connection[1].send(players_choice)


    # Clean Up
    log.info('Killing ViewModel Producer')
    viewmodelProducer.stopProducing()
    log.info('Killing Model Producer')
    modelProducer.join()
    log.info('Done. Session %s' % (dt.now() - start))
