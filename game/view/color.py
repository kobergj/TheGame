import switch as s


class Colorizer:
    def __init__(self, **colorschemes):
        for name, scheme in colorschemes.iteritems():
            switch = s.Switch(*scheme)
            setattr(self, name, switch)

