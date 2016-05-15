

class Goods:
    MinSellPrice = 1
    MaxSellPrice = 3

    MinBuyPrice = 6
    MaxBuyPrice = 11

    ListOfNames = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']


class Rooms:
    RoomNameParts = {
        'cargoCapacity':        ['Cargo', 'Storage', 'Tool'],
        'maxTravelDistance':    ['Sensor', 'Scanning', 'Energy'],
        'attackPower':          ['Weapon', 'Gun', 'Torpedo'],
        'shieldStrength':       ['Shield', 'Reactor', 'Armor'],

        'roomType':             ['Bay', 'Array', 'Hub', 'Device', 'Room']
        }

    StatBoosts = {
        'cargoCapacity':        [5, 10],
        'maxTravelDistance':    [1, 4],
        'attackPower':          [3, 6],
        'shieldStrength':       [2, 6]
    }
