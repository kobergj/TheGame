import helpers.setup as h
import models.models as m
import implementations.factory as f

import game as g
import sys

PLAYERNAME = "Players Name"

UNIVERSENAME = ["Pegasus"]
SAMPLECARGO = ["Sample Cargo", "Another Cargo"]
SAMPLEHARBORS = ["Safe Harbor", "Even safer Harbor"]

STARTCURRENCY = [m.Currency("Credits"), 12]


if __name__ == '__main__':
    h.SetUp(sys.argv)

    game = g.Game(
        player=m.Player(
            name=PLAYERNAME,
            startCurrency=STARTCURRENCY,
        ),
        universe=m.Universe(
            name=UNIVERSENAME,
            harborfactory=f.HarborFactory(SAMPLEHARBORS, f.CargoFactory(SAMPLECARGO)).RandomHarbor,
        )
    )

    while game:
        # Lean Back and relax
        pass
