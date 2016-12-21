

class Goods:
    MinSellPrice = 1
    MaxSellPrice = 3

    MinBuyPrice = 6
    MaxBuyPrice = 11

    MinPrice = 1
    MaxPrice = 14

    ListOfNames = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']


class Rooms:
    # RoomNameParts = {
    #     'cargoCapacity':        ['Cargo', 'Storage', 'Tool'],
    #     'maxTravelDistance':    ['Sensor', 'Scanning', 'Energy'],
    #     'attackPower':          ['Weapon', 'Gun', 'Torpedo'],
    #     'shieldStrength':       ['Shield', 'Reactor', 'Armor'],

    #     'roomType':             ['Bay', 'Array', 'Hub', 'Device', 'Room']
    #     }

    # StatBoosts = {
    #     'cargoCapacity':        [5, 10],
    #     'maxTravelDistance':    [1, 4],
    #     'attackPower':          [3, 6],
    #     'shieldStrength':       [2, 6]
    # }

    class EnergyCore:
        Capacity = [3, 20]

        PricePerCapacity = [80, 85]
        Energy = [-4, -1]

    class Engine:
        Capacity = [1, 8]

        PricePerCapacity = 125
        Energy = [1, 5]

    class CargoBay:
        Capacity = [4, 15]

        PricePerCapacity = [70, 75]
        Energy = [0, 0]

    class Shield:
        Capacity = [8, 18]

        PricePerCapacity = [70, 90]
        Energy = [0, 0]

    class Weapon:
        Capacity = [[1,10], [10,20]]

        PricePerCapacity = [90, 110]
        Energy = [1, 5]


