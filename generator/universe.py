import generator.planets as gpl
import generator.spacegates as gsg
import database.database as db


def generateUniverseInformation(numberOfPlanets, numberOfSpacegates):
    # generate List of Planets
    listOfPlanets = gpl.generatePlanetList(numberOfPlanets)

    # generate List of Spacegates
    listOfSpacegates = gsg.generateSpacegateList(numberOfSpacegates)

    # generate Universe Dict
    universeInfos = {'planets': listOfPlanets,
                     'spacegates': listOfSpacegates,

                     'maxCoordinates': db.Universe.MaxCoordinates,
                     'minCoordinates': db.Universe.MinCoordinates}

    return universeInfos
