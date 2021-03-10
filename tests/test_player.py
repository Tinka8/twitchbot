import unittest

from opendota.player import Player

fatallik = Player(42943450)

class TestPlayer(unittest.TestCase):
    def test_player(self):
        """
        Test that player has name
        """
        self.assertIsInstance(fatallik.name(), str)

    def test_estimated_mmr(self):
        """
        Test that player has MMR
        """
        self.assertIsInstance(fatallik.mmr(), int)

    def test_estimated_mmr_higher_than_minimum(self):
        """
        Test that player has MMR of atleast Guardian rank
        """
        self.assertTrue(fatallik.mmr() > 1000)

    def test_estimated_mmr_lower_than_maximum(self):
        """
        Test that player has MMR lower than some max expected number
        """
        self.assertTrue(fatallik.mmr() < 11000)

    def test_last_login(self):
        """
        Test that player has last login
        """
        self.assertIsInstance(fatallik.lastLogin(), str)


if __name__ == '__main__':
    unittest.main()