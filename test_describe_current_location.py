import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import describe_current_location


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_at_entrance(self, mock_output):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        expected_output = 'You stand at the entrance, start your advance to SE corner.\n'
        expected_output += '\n'
        expected_output += 'You are at X: 0, Y: 0.\n'
        describe_current_location(character)
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_entrance(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        expected_output = 'You are at X: 1, Y: 1.\n'
        describe_current_location(character)
        self.assertEqual(expected_output, mock_output.getvalue())


if __name__ == "__main__":
    main()
