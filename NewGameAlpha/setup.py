import terminal as t
import logging as logging


def SetUp(commandlineargs):
    logging.basicConfig(filename='logbook.log', filemode='w', level=logging.DEBUG)
    logging.critical('Logbook Initialized')

    return t.Terminal()
