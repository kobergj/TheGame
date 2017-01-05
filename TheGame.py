import setup as h
import interfaces as p
import view as v

import sys

if __name__ == '__main__':
    h.SetUp(sys.argv)

    logic = p.LogicInterface()

    view = v.ViewInterface()

    while view:
        view(logic)
