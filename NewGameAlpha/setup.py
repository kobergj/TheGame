import terminal as t
import logging as logging


def SetUp(commandlineargs):
    logging.basicConfig(
        filename='logbook.log',
        filemode='w',
        level=logging.DEBUG,
        # format="[%(levelname)s] %(filename)s // %(funcName)s: %(message)s "
    )
    logging.critical('Logbook Initialized')

    return t.Terminal()
