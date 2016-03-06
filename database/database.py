
class DynamicDatabase:
    class Goods:
        MinNumberOfGoodsConsumed = 1
        MaxNumberOfGoodsConsumed = 3

        MinNumberOfGoodsProduced = 1
        MaxNumberOfGoodsProduced = 3

        MinSellPrice = 1
        MaxSellPrice = 3

        MinBuyPrice = 6
        MaxBuyPrice = 11

        ListOfNames = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']

    class Planets:
        ListOfNames = ['Earth', 'Venus', 'Mars', 'SecretPlanet', 'A3X-424', 'Eden', 'Volcan', 'Endar',
                       'Uranus', 'BingoPlanet', 'CrappyWorld']

    class Universe:
        MaxCoordinates = [10, 10]
        MinCoordinates = [0, 0]

        RestrictedCoordinates = list([0, 0])

        EnemyProbability = 50

        AnomalyTypes = ['Planet', 'Planet', 'Planet', 'Spacegate', 'Starbase', 'Starbase']

    class Ships:
        Cargobounds = [6, 15]
        Speedbounds = [1, 3]
        Travelbounds = [2, 4]
        Roombounds = [2, 4]
        Attackbounds = [3, 6]
        Shieldbounds = [8, 14]

    class Spacegates:
        IdentifiersList = ['SPG-#']

        CostForUse = 0

    class Starbases:
        ListOfNames = ['CC2', 'LaCathedral', 'TravelersInn', 'GlibberStation', 'MaggysDiner', 'Nine-Ty-Nine']
