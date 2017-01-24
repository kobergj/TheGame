import logging as logging

import kindaconfiguration as conf
# Configuration Access
FUNCTIONUPLOG = conf.Logger.FuntionInvokedLogMessage
FUNCTIONDONELOG = conf.Logger.FunctionFinishedLogMessage
# Configuration Access End


def InitLoggers(logconfig):
    # Working with only one Logger at the Moment
    # Should be Improved
    logging.basicConfig(
        filename=logconfig.LogFile,
        filemode=logconfig.WriteMode,
        level=logconfig.Level,
        format=logconfig.Format,
    )
    logging.critical(logconfig.OnInitMessage)


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
