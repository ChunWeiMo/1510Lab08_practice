import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import describe_current_hp


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_positive_hp(self, mock_output):
        character = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 5}
        describe_current_hp(character)
        expected_output = 'Your current HP: 5\n\n'
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_0_hp(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 4, 'Current HP': 0}
        describe_current_hp(character)
        expected_output = 'Your current HP: 0\n\n'
        self.assertEqual(expected_output, mock_output.getvalue())


if __name__ == "__main__":
    main()
