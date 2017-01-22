import helpers.setup as h
import models.models as m
import implementations.factory as f

import game as g
import sys

import helpers.kindaconfiguration as conf
# Configuration Access
PLAYERNAME = conf.Initial.PlayerName
UNIVERSENAME = conf.Initial.UniverseName
SAMPLECARGO = conf.Cargo.Names
SAMPLEHARBORS = conf.Harbors.Names
STARTCREDITS = conf.Initial.StartCredits
CREDITS = conf.Currencies.Credits
CARGOCAPACITY = conf.Initial.CargoCap
# Configuration Access End

STARTCURRENCY = [[m.Currency(CREDITS), STARTCREDITS]]

if __name__ == '__main__':
    h.SetUp(sys.argv)

    game = g.Game(
        player=m.Player(
            name=PLAYERNAME,
            startCurrency=STARTCURRENCY,
            cargocap=CARGOCAPACITY,
        ),
        universe=m.Universe(
            name=UNIVERSENAME,
            harborfactory=f.HarborFactory(SAMPLEHARBORS, f.CargoFactory(SAMPLECARGO)).RandomHarbor,
        )
    )

    while True:
        # Lean Back and relax
        game()
