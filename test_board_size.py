from unittest import TestCase
from unittest import main
from simple_game import board_size


class Test(TestCase):
    def test_2_by_2_board(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room',
                 (1, 0): 'Spike trap', (1, 1): 'Goal'}
        expected_wall = (1, 1)
        self.assertAlmostEqual(expected_wall, board_size(board))

    def test_square_board(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Spike trap', (0, 2): 'Empty room', (1, 0): 'Spirit fountain', (
            1, 1): 'Spirit fountain', (1, 2): 'Poison gas', (2, 0): 'Camp fire', (2, 1): 'Empty room', (2, 2): 'Goal'}
        expected_wall = (2, 2)
        self.assertAlmostEqual(expected_wall, board_size(board))

    def test_rows_grater_than_columns_board(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Camp fire', (0, 2): 'Poison gas', (1, 0): 'Spike trap', (1, 1):
                 'Spirit fountain', (1, 2): 'Poison gas', (2, 0): 'Camp fire', (2, 1): 'Empty room', (2, 2):
                 'Spirit fountain', (3, 0): 'Spike trap', (3, 1): 'Spike trap', (3, 2): 'Goal'}
        expected_wall = (3, 2)
        self.assertAlmostEqual(expected_wall, board_size(board))

    def test_rows_less_than_columns_board(self):
        board = {(0, 0): 'Entrance', (0, 1): 'Camp fire', (0, 2): 'Spirit fountain', (0, 3): 'Poison gas',
                 (1, 0): 'Spirit fountain', (1, 1): 'Spirit fountain', (1, 2): 'Empty room',
                 (1, 3): 'Spike trap', (2, 0): 'Spirit fountain', (2, 1): 'Empty room',
                 (2, 2): 'Poison gas', (2, 3): 'Goal'}
        expected_wall = (2, 3)
        self.assertAlmostEqual(expected_wall, board_size(board))


if __name__ == "__main__":
    main()
