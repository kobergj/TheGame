import helpers.setup as h
import controllers.logic as c
import view.logic as v
import models.models as m

import sys

PLAYERNAME = "Players Name"

UNIVERSENAME = ["Pegasus"]
SAMPLECARGO = [[m.Cargo("Sample Cargo"), 1], [m.Cargo("Another Cargo"), 1]]
SAMPLEHARBORS = [[m.Harbor("Safe Harbor"), 1], [m.Harbor("Even safer Harbor"), 0]]

STARTCURRENCY = [m.Currency("Credits"), 12]


if __name__ == '__main__':
    h.SetUp(sys.argv)

    player = m.Player(
        name=PLAYERNAME,
        startCurrency=STARTCURRENCY,
    )

    universe = m.Universe(
        name=UNIVERSENAME,
        harbors=SAMPLEHARBORS,
        cargos=SAMPLECARGO
    )

    logic = c.LogicController(player, universe)

    view = v.LogicViewer(player, universe)

    while view:
        view(logic)
