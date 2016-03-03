import visualization.starbases as viz
import generator.ships as gsh
import generator.rooms as gro
import models.ships as msh
import models.rooms as mro


def Arrive(Starbase, Player):
    # Generate Ship
    ship = gsh.generateShipInformation()

    # Attach Ship to Station
    Starbase.changeShipForSale(msh.Ship(ship))

    # Fill Room List
    while len(Starbase.roomsForSale) < Starbase.maxRoomsForSale:
        # Create Room
        room = gro.generateRoomInformation()

        # Add Room
        Starbase.addRoomForSale(mro.Room(room))

    while True:
        # Define Possible Actions
        possibleActions = {'quit': Quit,
                           'inspectShip': InspectShip,
                           'inspectRooms': InspectRooms,
                           'depart': Depart
                           }

        # Await Player Choice
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
    print choice

    # Execute Choice
    possibleActions[choice](Starbase, Player)


def RefuseShip(Starbase, Player):
    pass


def AcceptShip(Starbase, Player):
    # Spend Credits
    Player.spendCredits(Player.currentShip.price)

    # Switch Ship
    Player.switchShip(Starbase.shipForSale)

    Starbase.shipForSale = None


def InspectRooms(Starbase, Player):
    viz.buyRooms(Starbase, Player)
