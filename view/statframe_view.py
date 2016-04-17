

class StatView:
    playerStatsTemplate ="""

    Current Stats:
    Credits: %(credits)s    Attack:  %(attackPower)s    Defense: %(curDef)s/%(maxDef)s  Maximum Travel Distance: %(maxTravelDistance)s  Maintenance Costs: %(maintCosts)s

    Cargo Bay: %(currentCargo)s/%(maxCargo)s -> %(inCargo)s

    Rooms:  %(currentRooms)s/%(maxRooms)s -> %(roomList)s"""


    def __call__(self, Player):
        playerStats = {
            'credits': Player.credits,
            'attackPower': Player.currentShip.attackPower(),
            'curDef': Player.currentShip.shieldStrength(),
            'maxDef': Player.currentShip.shieldStrength.startValue,
            'maxTravelDistance': Player.currentShip.maxTravelDistance(),
            'maintCosts': Player.currentShip.maintenanceCosts(),
            'currentCargo': Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity(),
            'maxCargo': Player.currentShip.cargoCapacity.startValue,
            'inCargo': self.cargoString(Player.currentShip.inCargo),
            'currentRooms': Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms(),
            'maxRooms': Player.currentShip.spaceForRooms.startValue,
            'roomList': self.roomString(Player.currentShip.rooms)
        }

        return self.playerStatsTemplate % playerStats

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

