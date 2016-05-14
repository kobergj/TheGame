import multiprocessing as mp
from datetime import datetime as dt

import configuration.database as db
import logging

import controller.model_fabric as mf
import controller.viewmodel_fabric as vf

import view.basic_view as vwf

# Starting Time Stamp
start = dt.now()

# Init Log
logging.basicConfig(filename='configuration/basic.log', level=logging.INFO,
                    filemode='w', format='%(asctime)s, %(filename)s --  %(message)s')

logging.info('Init Database')
database = db.DynamicDatabase

logging.info('Creating Connections')
model_connection = mp.Pipe()
view_connection = mp.Pipe()

logging.info('Initialize Model Producer')
modelProducer = mf.randomProducer(database, model_connection[0])

logging.info('Initialize ViewModel Producer')
viewmodelProducer = vf.ViewModelProducer(model_connection[1], view_connection[0])

logging.info('Init View')
view = vwf.View(database)

if __name__ == '__main__':
    logging.info('Start Model Producer')
    modelProducer.startProducing()

    logging.info('Start ViewModel Producer')
    viewmodelProducer.startProducing()

    players_choice = True

    while players_choice is not None:
        # Get View Model
        view_model = view_connection[1].recv()
        # Show View Model
        players_choice = view(view_model)
        # Return Answer
        view_connection[1].send(players_choice)


    # Clean Up
    logging.info('Killing ViewModel Producer')
    viewmodelProducer.stopProducing()
    logging.info('Killing Model Producer')
    modelProducer.stopProducing()
    logging.info('Done. Session %s' % (dt.now() - start))