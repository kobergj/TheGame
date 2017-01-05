
import unittest
from nose_parameterized import parameterized, param

import container as c
import models.models as m


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
