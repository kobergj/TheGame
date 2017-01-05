

class StartConfiguration:
    # NumberOfAnomalies = 25

    # MaxCoordinates = [15, 15]
    # MinCoordinates = [0, 0]

    # PlayerInfo = {'name': 'Dr.Play',
    #                'startingCredits': 12
    #                }

    # StartingShipStats = {'cargoCapacity': 10,

    #                        'maintenanceCosts': 2,
    #                        'maxTravelDistance': 4,

    #                        'spaceForRooms': 2,

    #                        'price': 0,

    #                        'attackPower': 7,
    #                        'shieldStrength': 15,
    #                        }

    class Player:
        PlayerName = 'Dr.Play'
        PlayerCredits = 12

    class Ship:
        Name = 'Small Shuttle'

        # Stats: [Capacity, EnergyCosts]
        CargoBay = [10, 0]
        EnergyCore = [20, -2]
        Engine = [4, 2]
        Weapon = [[5,8], 2]
        Shield = [15, 0]

    class Universe:
        MaxCoordinates = [15, 15]
        MinCoordinates = [0, 0]

        NumberOfAnomalies = 15  # Should not be more than number of Names in anomaly_db

        # EnemyProbability = 10

class Enemies:
    Fractions = ['Raider', 'Slaver', 'Pirate', 'Legion', 'Royal Navy']
