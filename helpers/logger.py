import logging as logging

FUNCTIONUPLOG = "Function '%s' invoked with args %s and kwargs %s"
FUNCTIONERRORLOG = "Function '%s' threw Error %s"
FUNCTIONDONELOG = "Function '%s' finished with result %s"


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
