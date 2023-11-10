import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import move_character


class TestMoveCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 0
        move_character(character, direction)
        expect_character = {'X-coordinate': 1,
                            'Y-coordinate': 0, 'Current HP': 5}
        expect_message = 'moving toward North...\n'
        self.assertEqual(expect_character, character)
        self.assertEqual(expect_message, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 1
        move_character(character, direction)
        expect_character = {'X-coordinate': 2,
                            'Y-coordinate': 1, 'Current HP': 5}
        expect_message = 'moving toward East...\n'
        self.assertEqual(expect_character, character)
        self.assertEqual(expect_message, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 2
        move_character(character, direction)
        expect_character = {'X-coordinate': 1,
                            'Y-coordinate': 2, 'Current HP': 5}
        expect_message = 'moving toward South...\n'
        self.assertEqual(expect_character, character)
        self.assertEqual(expect_message, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west(self, mock_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 3
        move_character(character, direction)
        expect_character = {'X-coordinate': 0,
                            'Y-coordinate': 1, 'Current HP': 5}
        expect_message = 'moving toward West...\n'
        self.assertEqual(expect_character, character)
        self.assertEqual(expect_message, mock_output.getvalue())


if __name__ == "__main__":
    main()
