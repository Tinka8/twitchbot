import unittest

from resources.winsloses import getWinsAndLoses
from resources.winsloses import getRecentMatches

class TestWinsLoses(unittest.TestCase):
    def test_wins_is_number(self):
        """
        Test that wins is number
        """
        self.assertIsInstance(getWinsAndLoses(42943450, 1613844000)['wins'], int)

    def test_loses_is_number(self):
        """
        Test that loses is number
        """
        self.assertIsInstance(getWinsAndLoses(42943450, 1613844000)['loses'], int)

    def test_recent_matches_has_status_code_200(self):
        """
        Test that response from getRecentMatches has success HTTP response code
        """
        self.assertEqual(getRecentMatches(42943450).status_code, 200)


if __name__ == '__main__':
    unittest.main()
