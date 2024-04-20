import unittest
from vikingsClasses import War, Viking, Saxon
from inspect import signature


class TestWar(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.war = War()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(War).parameters), 0)

    def testVikingArmy(self):
        self.assertEqual(self.war.vikingArmy, [])

    def testSaxonArmy(self):
        self.assertEqual(self.war.saxonArmy, [])


if __name__ == '__main__':
    unittest.main()
