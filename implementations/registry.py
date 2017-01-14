import helpers.logger as log


class ExecRegistry:
    def __init__(self, keyfunc):
        self._infodict = dict()
        self._execdict = dict()

        self._keyfunc = keyfunc

    def __iter__(self):
        for key in self._execdict:
            yield key, self[key]

    def __getitem__(self, key):
        return self._infodict[key]

    def __call__(self, key):
        exe = self._execdict[key]
        return exe()

    def __contains__(self, key):
        return key in self._execdict

    @log.Logger('Register Exec Func')
    def Register(self, info, func, *args, **kwargs):
        key = self._keyfunc(info)

        self._infodict[key] = info

        def execute():
            return func(*args, **kwargs)

        self._execdict[key] = execute

        return key
