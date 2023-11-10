from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import get_user_choice


class Test(TestCase):
    @patch('builtins.input', side_effect=[0])
    def test_input_0(self, _):
        expected = 0
        self.assertEqual(expected, get_user_choice())

    @patch('builtins.input', side_effect=[1])
    def test_input_1(self, _):
        expected = 1
        self.assertEqual(expected, get_user_choice())

    @patch('builtins.input', side_effect=[2])
    def test_input_2(self, _):
        expected = 2
        self.assertEqual(expected, get_user_choice())

    @patch('builtins.input', side_effect=[3])
    def test_input_3(self, _):
        expected = 3
        self.assertEqual(expected, get_user_choice())

    @patch('builtins.input', side_effect=[5])
    def test_input_not_illegal(self, _):
        with self.assertRaises(StopIteration):
            get_user_choice()


if __name__ == "__main__":
    main()
