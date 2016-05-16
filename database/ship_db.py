

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
