import generator.planets as gpl
import generator.spacegates as gsg
import generator.starbases as gsb
import database.database as db


def generateUniverseInformation(numberOfPlanets, numberOfSpacegates, numberOfStarbases):
    # generate List of Planets
    listOfPlanets = gpl.generatePlanetList(numberOfPlanets)

    # generate List of Spacegates
    listOfSpacegates = gsg.generateSpacegateList(numberOfSpacegates)

    # generate List of Starbases
    listOfStarbases = gsb.generateStarbaseList(numberOfStarbases)

    # generate Universe Dict
    universeInfos = {'anomalyInformations': {
                        'Planet': listOfPlanets,
                        'Spacegate': listOfSpacegates,
                        'Starbase': listOfStarbases
                        },

                     'maxCoordinates': db.Universe.MaxCoordinates,
                     'minCoordinates': db.Universe.MinCoordinates}

    return universeInfos
