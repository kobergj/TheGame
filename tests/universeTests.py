import unittest
import models.universe as uvs
import errors as err

GENERIC_PLANET_NAME = 'Earth'
GENERIC_GOODS_CONSUMED = ['Videogames']
GENERIC_GOODS_PRODUCED = ['Gin']
GENERIC_PLANET_COORDINATES = [0, 1, 0]

GENERIC_PLANET_NAME_TWO = 'Mars'
GENERIC_GOODS_CONSUMED_TWO = ['Gin']
GENERIC_GOODS_PRODUCED_TWO = ['Sand', 'Evil']
GENERIC_PLANET_COORDINATES_TWO = [0, 1, 3]


GENERIC_PLANET_INFO = {'name': GENERIC_PLANET_NAME,
                       'goodsConsumed': GENERIC_GOODS_CONSUMED,
                       'goodsProduced': GENERIC_GOODS_PRODUCED,
                       'coordinates': GENERIC_PLANET_COORDINATES}

GENERIC_PLANET_INFO_TWO = {'name': GENERIC_PLANET_NAME_TWO,
                           'goodsConsumed': GENERIC_GOODS_CONSUMED_TWO,
                           'goodsProduced': GENERIC_GOODS_PRODUCED_TWO,
                           'coordinates': GENERIC_PLANET_COORDINATES_TWO}


GENERIC_ANOMALIE_INFORMATIONS = {'planets': [GENERIC_PLANET_INFO, GENERIC_PLANET_INFO_TWO]}


class universeInitialisationTests(unittest.TestCase):
    def test_planetIsGenerated(self):
        expected = 'Earth'
        universe = uvs.Universe(GENERIC_ANOMALIE_INFORMATIONS)
        self.assertEqual(universe.__dict__[GENERIC_PLANET_NAME].Name, expected,
                         err.NOT_EQUAL('initPlanets', universe.__dict__[GENERIC_PLANET_NAME].Name, expected))

    def test_planetListIsGenerated(self):
        expected = [GENERIC_PLANET_NAME, GENERIC_PLANET_NAME_TWO]
        universe = uvs.Universe(GENERIC_ANOMALIE_INFORMATIONS)
        self.assertEqual(universe.planetList, expected,
                         err.NOT_EQUAL('planetList', universe.planetList, expected))


if __name__ == '__main__':
    unittest.main(verbosity=2)
