
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
                m.Cargo('Some Cargo'): 4,
            },
        ),
        param(
            item=m.Cargo('Some Cargo'),
            amount=21,
            initial={
                m.Cargo('Some Cargo'): 4,
            },
            expected={
                m.Cargo('Some Cargo'): 25,
            }
        ),
        param(
            item=m.Cargo('Some Cargo'),
            amount=1,
            initial={
                m.Cargo('Some Cargo'): 4,
                m.Cargo('Another Cargo'): 12,
            },
            expected={
                m.Cargo('Some Cargo'): 5,
                m.Cargo('Another Cargo'): 12,
            }
        ),
    ])
    def test_manipulate(self, item, amount, initial, expected):
        container = c.Container()
        container._items = initial

        # Test
        container.manipulate(item, amount)

        self.assertEqual(container._items, expected)
