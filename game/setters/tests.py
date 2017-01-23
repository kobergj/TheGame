import unittest
from nose_parameterized import parameterized, param

import models.models as m
import player as p


class PlayerControllerTests(unittest.TestCase):

    @parameterized.expand([
        param(
            item=m.Cargo('Some Cargo'),
            credits=-2,
            startArgs=[
                m.Player(''),
            ],
            expectedCredits=2,
            expectedAmount=1
        ),
        param(
            item=m.Cargo('Some Cargo'),
            credits=91,
            startArgs=[
                m.Player(''),
            ],
            expectedCredits=103,
            expectedAmount=10
        ),
        param(
            item=m.Cargo('Some Cargo'),
            credits=-11,
            startArgs=[
                m.Player(''),
            ],
            expectedCredits=1,
            expectedAmount=1
        ),
    ])
    def test_trade(self, item, credits, startArgs, expectedCredits, expectedAmount):
        player = p.PlayerController(*startArgs)

        player.Trade(credits, item)

        self.assertEqual(player._currencyController.GetCredits(), expectedCredits)

        actualAmount = player._cargoController._cargo[item]
        self.assertEqual(actualAmount, expectedAmount)


"""
    @parameterized.expand([
        param(
            action=a.BuyItem('', m.Cargo('Some Cargo', 3)),
            credits=5,
            expected=True,
        ),
    ])
    def test_buyitem_available(self, action, credits, expected):
        player = i.PlayerInterface('')

        player.Credits(credits)

        actual = action.available(player)

        self.assertEqual(actual, expected)
"""
