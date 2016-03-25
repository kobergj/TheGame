import logging

def initLogBook():

    logging.basicConfig(filename='logbook/basic.log', level=logging.INFO,
                        filemode='w', format='%(asctime)s, %(message)s')

    logging.warning('-- -- LOGBOOK INITIALIZED -- --')


def log(message):

    logging.info(message)


class FleeError(AssertionError):
    pass

class DepartError(AssertionError):
    pass
