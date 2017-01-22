import helpers.setup as h
import models.models as m
import implementations.factory as f

import game as g
import sys

import helpers.kindaconfiguration as conf
# Configuration Access
PLAYERNAME = conf.Initial.PlayerName
UNIVERSENAME = conf.Initial.UniverseName
STARTCREDITS = conf.Initial.StartCredits
CARGOCAPACITY = conf.Initial.CargoCap
CARGOCAPNAME = conf.Stats.CargoCapacity
TRAVELCOST = conf.Initial.TravelCosts
TRAVELCOSTNAME = conf.Stats.TravelCosts
SAMPLECARGO = conf.Cargo.Names
SAMPLEHARBORS = conf.Harbors.Names
CREDITS = conf.Currencies.Credits
STARTSHIPNAME = conf.Initial.StartShipName
# Configuration Access End

STARTCURRENCY = [[m.Currency(CREDITS), STARTCREDITS]]
STARTSHIP = [m.Ship(STARTSHIPNAME, {CARGOCAPNAME: CARGOCAPACITY, TRAVELCOSTNAME: TRAVELCOST}), 1]

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
        ),
        fleet=m.Fleet(
            ships=[STARTSHIP])
    )

    while True:
        # Lean Back and relax
        game()
