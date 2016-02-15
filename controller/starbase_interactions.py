import visualization.starbases as viz
import generator.ships as gsh
import models.ships as mod


def Arrive(Starbase, Player):
    # Generate Ship
    ship = gsh.generateShipInformation()

    # Attach Ship to Station
    Starbase.changeShipForSale(mod.Ship(ship))

    while True:
        # Define Possible Actions
        possibleActions = {'quit': Quit,
                           'inspectShip': InspectShip,
                           'depart': Depart
                           }

        # Await Player Choose
        choice = viz.starbaseArrival(Starbase, Player)

        # Execute Choice
        killSwitch = possibleActions[choice](Starbase, Player)

        if killSwitch:
            return


def Depart(Planet, Player):
    return True


def Quit(Planet, Player):
    quit()


def InspectShip(Starbase, Player):
    # Define Possible Actions
    possibleActions = {'refuse': RefuseShip,
                       'accept': AcceptShip
                       }

    # Await Players Choice
    choice = viz.buyShip(Starbase, Player)

    # Execute Choice
    possibleActions[choice](Starbase, Player)


def RefuseShip(Starbase, Player):
    pass


def AcceptShip(Starbase, Player):
    pass
