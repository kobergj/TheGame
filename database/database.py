
class DynamicDatabase:
    class Goods:
        MinSellPrice = 1
        MaxSellPrice = 3

        MinBuyPrice = 6
        MaxBuyPrice = 11

        ListOfNames = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']

    class Planets:
        MinNumberOfGoodsConsumed = 1
        MaxNumberOfGoodsConsumed = 3

        MinNumberOfGoodsProduced = 1
        MaxNumberOfGoodsProduced = 3

        ListOfNames = ['Earth', 'Venus', 'Mars', 'SecretPlanet', 'A3X-424', 'Eden', 'Volcan', 'Endar',
                       'Uranus', 'BingoPlanet', 'CrappyWorld']

    class Universe:
        EnemyProbability = 10

        AnomalyTypes = ['Planet', 'Planet', 'Planet', 'Spacegate', 'Starbase', 'Starbase']

    class Ships:
        ShipClasses = ['Shuttle', 'Freighter', 'Scout', 'Viper']

        # Generic Stats
        cargoCapacity = 10
        spaceForRooms = 3

        # Movement
        maintenanceCosts = 5
        maxTravelDistance = 3

        # Battle
        attackPower = 5
        shieldStrength = 10

        class Shuttle:
            """Small Shuttle. Average Stats."""
            bounds = {
                'cargoCapacity':        [-2, 2],
                'spaceForRooms':        [-1, 1],

                'maintenanceCosts':     [-1, 1],
                'maxTravelDistance':    [-1, 1],

                'attackPower':          [-2, 2],
                'shieldStrength':       [-3, 3],
            }

        class Freighter:
            """Big Cargo loads. Slow & Expansive."""
            bounds = {
                'cargoCapacity':        [3, 10],
                'spaceForRooms':        [0, 2],

                'maintenanceCosts':     [0, 4],
                'maxTravelDistance':    [-2, 1],

                'attackPower':          [-3, 1],
                'shieldStrength':       [-1, 4],
            }

        class Scout:
            """Fast Ship. Perfekt for Exploring."""
            bounds = {
                'cargoCapacity':       [-6, -2],
                'spaceForRooms':        [-1, 1],

                'maintenanceCosts':     [-4, 0],
                'maxTravelDistance':    [0, 3],

                'attackPower':          [-1, 2],
                'shieldStrength':       [-2, 1],
            }

        class Viper:
            """Fast Attack Ship. Dont let them hit you"""
            bounds = {
                'cargoCapacity':        [-8, -4],
                'spaceForRooms':        [-2, 0],

                'maintenanceCosts':     [-3, -1],
                'maxTravelDistance':    [-2, 1],

                'attackPower':          [2, 5],
                'shieldStrength':       [-4, 0],
            }

    class Enemies:
        Fractions = ['Raider', 'Slaver', 'Pirate', 'Legion', 'Royal Navy']

    class Spacegates:
        IdentifiersList = ['SPG-#']

        CostForUse = 0

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

    class Starbases:
        ListOfNames = ['CC2', 'LaCathedral', 'TravelersInn', 'GlibberStation', 'MaggysDiner', 'Nine-Ty-Nine']
