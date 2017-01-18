import helpers.setup as h
import models.models as m
import implementations.factory as f

import game as g
import sys

PLAYERNAME = "Players Name"

UNIVERSENAME = ["Pegasus"]
SAMPLECARGO = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']
SAMPLEHARBORS = ['Earth', 'Venus', 'Mars', 'SecretPlanet', 'A3X-424', 'Eden', 'Volcan', 'Endar',
                 'Uranus', 'BingoPlanet', 'CrappyWorld', 'CC2', 'LaCathedral', 'TravelersInn',
                 'GlibberStation', 'MaggysDiner', 'Nine-Ty-Nine']

STARTCURRENCY = [[m.Currency("Credits"), 12]]


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

    while True:
        # Lean Back and relax
        game()
