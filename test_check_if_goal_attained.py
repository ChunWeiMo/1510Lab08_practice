import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attain_goal(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 1}
        expected_message = 'Congratulation! You achieve the goal!\n'
        self.assertEqual(True, check_if_goal_attained(board, character))
        self.assertEqual(expected_message, mock_output.getvalue())

    def test_not_attain_goal(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (
            1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Goal'}
        character = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 1}
        self.assertEqual(None, check_if_goal_attained(board, character))


if __name__ == "__main__":
    main()
