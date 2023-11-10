import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import validate_move


class TestValidateMove(TestCase):
    def test_valid_north(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 0
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))

    def test_valid_east(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 1
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))

    def test_valid_south(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 2
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))

    def test_valid_west(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 3
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stop_north(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        direction = 0
        expected_can_move = False
        expected_output = 'You are stopped by North wall\n\n'
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stop_east(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 1
        expected_can_move = False
        expected_output = 'You are stopped by East wall\n\n'
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stop_south(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
        direction = 2
        expected_can_move = False
        expected_output = 'You are stopped by South wall\n\n'
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stop_west(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 3
        expected_can_move = False
        expected_output = 'You are stopped by West wall\n\n'
        self.assertEqual(expected_can_move, validate_move(
            board, character, direction))
        self.assertEqual(expected_output, mock_output.getvalue())


if __name__ == "__main__":
    main()
