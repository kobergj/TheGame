import logging as logging

import kindaconfiguration as conf
# Configuration Access
LOGFILENAME = conf.Logger.LogFile
LOGFILEMODE = conf.Logger.WriteMode
LOGLEVEL = conf.Logger.Level
LOGFORMAT = conf.Logger.Format
LOGINITMESSAGE = conf.Logger.OnInitMessage
FUNCTIONUPLOG = conf.Logger.FuntionInvokedLogMessage
FUNCTIONDONELOG = conf.Logger.FunctionFinishedLogMessage
# Configuration Access End


def InitLoggers():
    # Working with only one Logger at the Moment
    # Should be Improved
    logging.basicConfig(
        filename=LOGFILENAME,
        filemode=LOGFILEMODE,
        level=LOGLEVEL,
        format=LOGFORMAT,
    )
    logging.critical(LOGINITMESSAGE)


class Logger:
    def __init__(self, identifier, logger=''):
        self.logger = logging.getLogger(logger)
        self.identifier = identifier

    def __call__(self, func):
        log = self.logger
        fn = self.identifier

        def newfunc(*args, **kwargs):
            log.info(FUNCTIONUPLOG % (fn, args, kwargs))

            result = func(*args, **kwargs)

            log.debug(FUNCTIONDONELOG % (fn, result))

            return result

        return newfunc
