

class StartConfiguration:
    NumberOfAnomalies = 25

    MaxCoordinates = [15, 15]
    MinCoordinates = [0, 0]

    PlayerInfo = {'name': 'Dr.Play',
                   'startingCredits': 12
                   }

    StartingShipStats = {'cargoCapacity': 10,

                           'maintenanceCosts': 2,
                           'maxTravelDistance': 4,

                           'spaceForRooms': 2,

                           'price': 0,

                           'attackPower': 7,
                           'shieldStrength': 15,
                           }

class Universe:
    EnemyProbability = 10

    AnomalyTypes = ['Planet', 'Planet', 'Planet', 'Spacegate', 'Starbase', 'Starbase']


class Enemies:
    Fractions = ['Raider', 'Slaver', 'Pirate', 'Legion', 'Royal Navy']
