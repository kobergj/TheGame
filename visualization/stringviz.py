

class Stringer:
    def __init__(self, start):
        self._string = CustomString(start)

    def __str__(self):
        return str(self._string)

    def BuyAction(self, buyreg):
        for key, info in buyreg:
            line = BUYMESSAGE % (key, info)
            self.AddLine(line)


class RegistryStringer:
    def __init__(self, infofunc, template):
        self._infofunc = infofunc
        self._strfactory = StringFactory(template)

    def __call__(self, registry):
        s = CustomString()
        for key, _ in registry:
            info = registry[key]
            args = self._infofunc(info)
            s += self._strfactory.NewString(*args)
        return s


class StringFactory:
    def __init__(self, template):
        self._template = template

    def NewString(self, *args):
        string = CustomString()
        string += self._template % args
        return string


class CustomString:
    def __init__(self, start=""):
        self._string = str(start)

    def __str__(self):
        return self._string

    def __iadd__(self, item):
        self._string += "\n"
        self._string += str(item)
