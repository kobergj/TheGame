import logger as log

import kindaconfiguration as conf


def SetUp(commandlineargs):
    log.InitLoggers(conf.Logger)
    return conf
