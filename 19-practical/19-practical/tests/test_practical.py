import unittest
from unittest.mock import Mock, patch

import practical.practical19

#Write unit tests for the Practical19 class using patch and Mock as necessary to implement the behaviour of datetime and random.
class TestPractical19(unittest.TestCase):
    def setUp(self):
        self.p = Practical19('example', 4)

    #def test__str__(self):
    #    return f'{self.name}: {self.num}'

    @patch('practical.practical19.random')
    def test_strange_number(self):
        mock_random.randint.return_value = 2
        result = self.p.strange_number(5)
        self.assertEqual(result, 7)

    @patch('practical.practical19.datetime')
    def test_is_it_the_weekend(self):
        mock_datetime.datetime.now.return_value = 7
        result = self.p.is_it_the_weekend()
        assertEqual(result, True) > 5 # Mon == 1, Sun == 7