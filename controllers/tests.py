import unittest
from nose_parameterized import parameterized, param

import models.models as m
import player as p


class PlayerControllerTests(unittest.TestCase):

    @parameterized.expand([
        param(
            item=m.Cargo('Some Cargo'),
            credits=-2,
            startCredits=4,
            expectedCredits=2,
            expectedAmount=1
        ),
        param(
            item=m.Cargo('Some Cargo'),
            credits=91,
            startCredits=12,
            expectedCredits=103,
            expectedAmount=-1
        ),
    ])
    def test_trade(self, item, credits, startCredits, expectedCredits, expectedAmount):
        player = p.PlayerController(m.Player(''))
        player._currencyController.TradeCredits(startCredits)

        player.Trade(credits, item)

        self.assertEqual(player._currencyController.GetCredits(), expectedCredits)

        self.assertEqual(player._cargoController.GetCargoAmount(item), expectedAmount)
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
