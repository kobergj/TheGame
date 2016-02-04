import unittest
import models.ships as s
import errors as err

GENERIC_CARGO_NAME = 'Gin'
GENERIC_CARGO_AMOUNT = 2

GENERIC_SHIP_CAPACITY = 10
GENERIC_SHIP_SPEED = 4

GENERIC_OVERLOAD_BONUS = 5
GENERIC_OVERLOAD_MALUS = 2

GENERIC_SHIP_STATS = {'cargoCapacity': GENERIC_SHIP_CAPACITY,
                      'speed': GENERIC_SHIP_SPEED,

                      'overloadbonus': GENERIC_OVERLOAD_BONUS,
                      'overloadmalus': GENERIC_OVERLOAD_MALUS}


class genericShip_methodTests(unittest.TestCase):
    # Tests regarding Method of class Ship()

    def test_loadCargoOnce(self):
        expected = {GENERIC_CARGO_NAME: GENERIC_CARGO_AMOUNT}
        genericShip = s.Ship(GENERIC_SHIP_STATS)
        genericShip.loadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        self.assertEqual(genericShip.inCargo, expected,
                         err.NOT_EQUAL('loadCargo', genericShip.inCargo, expected))

    def test_loadCargoTwice(self):
        expected = {GENERIC_CARGO_NAME: GENERIC_CARGO_AMOUNT*2}
        genericShip = s.Ship(GENERIC_SHIP_STATS)
        genericShip.loadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        genericShip.loadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        self.assertEqual(genericShip.inCargo, expected,
                         err.NOT_EQUAL('loadCargo', genericShip.inCargo, expected))

    def test_unloadCargoOnce(self):
        expected = {GENERIC_CARGO_NAME: GENERIC_CARGO_AMOUNT}
        genericShip = s.Ship(GENERIC_SHIP_STATS)
        genericShip.inCargo = {GENERIC_CARGO_NAME: GENERIC_CARGO_AMOUNT + GENERIC_CARGO_AMOUNT}
        genericShip.unloadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        self.assertEqual(genericShip.inCargo, expected,
                         err.NOT_EQUAL('unloadCargo', genericShip.inCargo, expected))

    def test_unloadCargoTwice(self):
        expected = {}
        genericShip = s.Ship(GENERIC_SHIP_STATS)
        genericShip.inCargo = {GENERIC_CARGO_NAME: GENERIC_CARGO_AMOUNT + GENERIC_CARGO_AMOUNT}
        genericShip.unloadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        genericShip.unloadCargo(GENERIC_CARGO_NAME, GENERIC_CARGO_AMOUNT)
        self.assertEqual(genericShip.inCargo, expected,
                         err.NOT_EQUAL('unloadCargo', genericShip.inCargo, expected))


class freighter_MethodTests(unittest.TestCase):
    # Tests regarding Methods of Class Freighter()

    def test_startOverloadRaisesCapacity(self):
        expected = GENERIC_SHIP_CAPACITY + GENERIC_OVERLOAD_BONUS
        freighter = s.Freighter(GENERIC_SHIP_STATS)
        freighter.startOverload()
        self.assertEqual(freighter.cargoCapacity, expected,
                         err.NOT_EQUAL('startOverload.Capacity', freighter.cargoCapacity, expected))

    def test_startOverloadLowersSpeed(self):
        expected = GENERIC_SHIP_SPEED - GENERIC_OVERLOAD_MALUS
        freighter = s.Freighter(GENERIC_SHIP_STATS)
        freighter.startOverload()
        self.assertEqual(freighter.speed, expected,
                         err.NOT_EQUAL('startOverload.Speed', freighter.speed, expected))


if __name__ == '__main__':
    unittest.main(verbosity=2)
