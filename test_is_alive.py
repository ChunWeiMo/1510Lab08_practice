import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import is_alive


class TestIsAlive(TestCase):
    def test_current_hp_positive(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 1}
        self.assertEqual(True, is_alive(character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_current_hp_0(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 0}
        expected_message = 'You dead...\n'
        expected_message += 'Close the game.\n'
        self.assertEqual(False, is_alive(character))
        self.assertEqual(expected_message, mock_output.getvalue())


if __name__ == "__main__":
    main()
