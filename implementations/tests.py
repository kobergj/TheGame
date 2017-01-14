
import unittest
from nose_parameterized import parameterized, param

import container as c
import queue as q
import registry as r

import models.models as m


# Test Helper to Mock Factory
class FakeFactory:
    def __init__(self, *robjects):
        self.i = -1
        self.robjects = robjects

    def __call__(self):
        self.i += 1
        return self.robjects[self.i]


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


class RefillingQueueTests(unittest.TestCase):
    @parameterized.expand([
        param(
            amount=1,
            factory=FakeFactory(1),
            cache=0,
            expectedResult=[1],
            expectedQueue=[],
        ),
        param(
            amount=3,
            factory=FakeFactory(4, 5, 6, '77', '111', '2364'),
            cache=1,
            expectedResult=[4, 5, 6],
            expectedQueue=['77'],
        ),
        param(
            amount=3,
            factory=FakeFactory(1, 2, 3, 0, 0, 1, '2', '0'),
            cache=5,
            expectedResult=[1, 2, 3],
            expectedQueue=[0, 0, 1, '2', '0'],
        ),
    ])
    def test_get(self, amount, factory, cache, expectedResult, expectedQueue):
        queue = q.RefillingQueue(factory, cache)

        # Test
        actualResult = list(queue.Get(amount))

        self.assertEqual(actualResult, expectedResult)

        self.assertEqual(queue._lifeline, expectedQueue)


class RegistryTests(unittest.TestCase):
    @parameterized.expand([
        param(
            info='Simple Info',
            func=lambda x: x,
            fargs=['44'],
            fkwargs={},
            expinfo='Simple Info',
            expfresult='44',
        ),
        param(
            info='Another Info',
            func=lambda x, y: x+y,
            fargs=[11, 23],
            fkwargs={},
            expinfo='Another Info',
            expfresult=34,
        ),
    ])
    def test_register(self, info, func, fargs, fkwargs, expinfo, expfresult):
        reg = r.ExecRegistry(lambda x: 0)

        # Test
        key = reg.Register(info, func, *fargs, **fkwargs)

        self.assertEqual(reg[key], expinfo)

        self.assertEqual(reg(key), expfresult)





