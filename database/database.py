
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


class Ships:
    Cargobounds = [6, 15]
    Speedbounds = [1, 3]
    Travelbounds = [2, 4]
    Roombounds = [2, 4]


class Spacegates:
    Identifiers = 'SPG-#XX'

    CostForUse = 0


class Starbases:
    ListOfNames = ['CC2', 'LaCathedral', 'TravelersInn', 'GlibberStation', 'MaggysDiner', 'Nine-Ty-Nine']


class Visualization:
    mapIdentifiers = {'Empty': '',
                      'Planet': '(00)',
                      'Spacegate': '[00]',
                      'Starbase': '$00$',
                      }
