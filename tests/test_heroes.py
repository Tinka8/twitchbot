import unittest

from resources.heroes import flatten
from resources.heroes import heroes
from resources.heroes import structuredHeroes

class TestHeroes(unittest.TestCase):
    def test_heroes_flatten(self):
        """
        Test that length of flatten heroes is same as heroes length
        """
        self.assertEqual(len(flatten(structuredHeroes)), len(heroes))

    def test_heroes_integrity(self):
        """
        Test that length of flatten heroes is 120 playable characters as there are in dota
        """
        self.assertEqual(len(heroes), 120)

if __name__ == '__main__':
    unittest.main()
    