import logging as logging

FUNCTIONUPLOG = "Function '%s' invoked with args %s and kwargs %s"
FUNCTIONERRORLOG = "Function '%s' threw Error %s"
FUNCTIONDONELOG = "Function '%s' finished with result %s"


class Logger:
    def __init__(self, name=''):
        self.logger = logging.getLogger(name)

    def __call__(self, func):
        log = self.logger
        fn = func.__name__

        def newfunc(*args, **kwargs):
            log.info(FUNCTIONUPLOG % (fn, args, kwargs))

            try:
                result = func(*args, **kwargs)
            except Exception as error:
                log.error(FUNCTIONERRORLOG % (fn, error))
                raise error

            log.debug(FUNCTIONDONELOG % (fn, result))

            return result

        return newfunc
