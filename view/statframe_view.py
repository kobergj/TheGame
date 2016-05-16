



def stat_view(Player, db=None):
    playerStats = {
        'credits': Player.credits,
        'attackPower': Player.currentShip.attackPower(),
        'curDef': Player.currentShip.shieldStrength(),
        'maxDef': Player.currentShip.shieldStrength.startValue,
        'maxTravelDistance': Player.currentShip.maxTravelDistance(),
        'maintCosts': Player.currentShip.maintenanceCosts(),
        'currentCargo': Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity(),
        'maxCargo': Player.currentShip.cargoCapacity.startValue,
        'inCargo': cargoString(Player.currentShip.inCargo),
        'currentRooms': Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms(),
        'maxRooms': Player.currentShip.spaceForRooms.startValue,
        'roomList': roomString(Player.currentShip.rooms)
    }

    return db.PlayerStatsTemplate % playerStats

def cargoString(CargoBay):
    cargo_string = ''

    for good_name, amount in CargoBay.iteritems():
        cargo_string += "%s: %s  " % (good_name, amount)

    return cargo_string

def roomString(Rooms):
    room_string = ''

    for room in Rooms:
        room_string += str(room.name)

        for statBoost in room.statBoosts:
            room_string += '-%s:%+d' %(statBoost.statName, statBoost.startValue)

        room_string += ' -- '

    return room_string

