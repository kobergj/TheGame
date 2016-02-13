import generator.planets as gpl
import database.database as db


def generateUniverseInformation(numberOfPlanets):
    # generate List of Planets
    listOfPlanets = gpl.generatePlanetList(numberOfPlanets)

    # generate Universe Dict
    universeInfos = {'planets': listOfPlanets,

                     'maxCoordinates': db.Universe.MaxCoordinates,
                     'minCoordinates': db.Universe.MinCoordinates}

    return universeInfos
