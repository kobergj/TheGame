
import unittest
from nose_parameterized import parameterized, param

import gamestats as c
import models as m
import actions as a
import player as p


class ContainerTests(unittest.TestCase):
    @parameterized.expand([
        param(
            item=m.Cargo('Some Cargo'),
            amount=4,
            initial={},
            expected={
                'Some Cargo': [m.Cargo('Some Cargo'), 4],
            },
        ),
        param(
            item=m.Cargo('Some Cargo'),
            amount=21,
            initial={
                'Some Cargo': [m.Cargo('Some Cargo'), 4],
            },
            expected={
                'Some Cargo': [m.Cargo('Some Cargo'), 25],
            }
        ),
        param(
            item=m.Cargo('Some Cargo'),
            amount=1,
            initial={
                'Some Cargo': [m.Cargo('Some Cargo'), 4],
                'Another Cargo': [m.Cargo('Another Cargo'), 12]
            },
            expected={
                'Some Cargo': [m.Cargo('Some Cargo'), 5],
                'Another Cargo': [m.Cargo('Another Cargo'), 12],
            }
        ),
    ])
    def test_manipulate(self, item, amount, initial, expected):
        container = c.Container()
        container._items = initial

        # Test
        container.manipulate(item, amount)

        self.assertEqual(container._items, expected)


class ActionTests(unittest.TestCase):

    @parameterized.expand([
        param(
            item=m.Cargo('Some Cargo', 2),
            player=p.Player('Some Player', None),
            startCredits=4,
            expectedCredits=6,
            expectedCargo={
                'Some Cargo': [m.Cargo('Some Cargo'), 1]
            },
        ),
        param(
            item=m.Cargo('Some Cargo', 91),
            player=p.Player('Some Player', None),
            startCredits=12,
            expectedCredits=103,
            expectedCargo={
                'Some Cargo': [m.Cargo('Some Cargo'), 1]
            },
        ),
    ])
    def test_buyitem(self, item, player, startCredits, expectedCredits, expectedCargo):
        action = a.BuyItem('BuyItem', item)

        player.Credits(startCredits)

        action(player)

        self.assertEqual(player.Credits(), expectedCredits)

        self.assertEqual(player.Cargo()._items, expectedCargo)
