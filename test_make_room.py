from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import make_room


class Test(TestCase):
    @patch('random.randint', return_value=0)
    def test_make_empty_room(self, _):
        actual = make_room()
        expected = 'Empty room'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_make_empty_room(self, _):
        actual = make_room()
        expected = 'Spike trap'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_make_empty_room(self, _):
        actual = make_room()
        expected = 'Poison gas'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_make_empty_room(self, _):
        actual = make_room()
        expected = 'Camp fire'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_make_empty_room(self, _):
        actual = make_room()
        expected = 'Spirit fountain'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
