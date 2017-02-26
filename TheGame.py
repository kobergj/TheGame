import helpers.setup as h
import models.models as m
import implementations.factory as f

import game.game as g
import pygameapi.pygameapi as pg
import view.view as v

import sys


if __name__ == '__main__':
    config = h.SetUp(sys.argv)

    controller = pg.PyGameApi(
        size=config.Layout.WindowSize,
        font=config.Layout.Font,
        fontsize=config.Layout.FontSize,
        bgcolor=config.Colors.Black
    )

    gamemodel = g.GameModel(
        pricerange=config.Limits.PriceRange,
        destnumber=config.Limits.NumberOfDestinations,
        statnames=config.Stats,
    )

    gamemodel.NewGame(
        player=m.Player(
            name=config.Initial.PlayerName,
            startCurrency=[
                [m.Currency(config.Currencies.Credits), config.Initial.StartCredits]],
        ),
        universe=m.Universe(
            name=config.Initial.UniverseName,
            harborfactory=f.HarborFactory(
                harbornames=config.Harbors.Names,
                cargofactory=f.CargoFactory(config.Cargo.Names)).RandomHarbor,
        ),
        fleet=m.Fleet(
            ships=[
                [
                    m.Ship(
                        name=config.Initial.StartShipName,
                        statdict={
                            config.Stats.CargoCapacity: config.Initial.CargoCap,
                            config.Stats.TravelCosts: config.Initial.TravelCosts,
                        },
                    ),
                    1
                ],
            ]
        ),
    )

    view = v.View(config.Images)

    while True:
        # Lean Back and relax
        view(gamemodel, controller)
