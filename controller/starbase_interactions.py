import visualization.starbases as viz


def Arrive(Starbase, Player):
    # Get Ship
    ship = Starbase.shipQ.get()

    # Attach Ship to Station
    Starbase.changeShipForSale(ship)

    # Fill Room List
    while len(Starbase.roomsForSale) < Starbase.maxRoomsForSale:
        # Get Room
        room = Starbase.roomQ.get()

        # Add Room
        Starbase.addRoomForSale(room)

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
