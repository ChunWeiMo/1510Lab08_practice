from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import make_board


class Test(TestCase):
    @patch('random.randint', side_effect=[0, 1])
    def test_2_by_2_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Empty room',
                        (1, 0): 'Spike trap', (1, 1): 'Goal'}
        self.assertEqual(except_board, make_board(2, 2))

    @patch('random.randint', side_effect=[1, 0, 4, 4, 2, 3, 0])
    def test_square_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Spike trap', (0, 2): 'Empty room', (1, 0): 'Spirit fountain', (
            1, 1): 'Spirit fountain', (1, 2): 'Poison gas', (2, 0): 'Camp fire', (2, 1): 'Empty room', (2, 2): 'Goal'}
        self.assertEqual(except_board, make_board(3, 3))

    @patch('random.randint', side_effect=[3, 2, 1, 4, 2, 3, 0, 4, 1, 1])
    def test_rows_grater_than_columns_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Camp fire', (0, 2): 'Poison gas', (1, 0): 'Spike trap', (1, 1):
                        'Spirit fountain', (1, 2): 'Poison gas', (2, 0): 'Camp fire', (2, 1): 'Empty room', (2, 2):
                        'Spirit fountain', (3, 0): 'Spike trap', (3, 1): 'Spike trap', (3, 2): 'Goal'}
        self.assertEqual(except_board, make_board(4, 3))

    @patch('random.randint', side_effect=[3, 4, 2, 4, 4, 0, 1, 4, 0, 2])
    def test_rows_less_than_columns_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Camp fire', (0, 2): 'Spirit fountain', (0, 3): 'Poison gas',
                        (1, 0): 'Spirit fountain', (1, 1): 'Spirit fountain', (1, 2): 'Empty room',
                        (1, 3): 'Spike trap', (2, 0): 'Spirit fountain', (2, 1): 'Empty room',
                        (2, 2): 'Poison gas', (2, 3): 'Goal'}
        self.assertEqual(except_board, make_board(3, 4))

    @patch('random.randint', side_effect=[0, 0])
    def test_all_same_room_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Empty room',
                        (1, 0): 'Empty room', (1, 1): 'Goal'}
        self.assertEqual(except_board, make_board(2, 2))

    @patch('random.randint', side_effect=[0, 1, 2, 3, 4, 0])
    def test_5_kinds_room_board(self, _):
        except_board = {(0, 0): 'Entrance', (0, 1): 'Empty room', (1, 0): 'Spike trap', (1, 1): 'Poison gas',
                        (2, 0): 'Camp fire', (2, 1): 'Spirit fountain', (3, 0): 'Empty room', (3, 1): 'Goal'}
        self.assertEqual(except_board, make_board(4, 2))


if __name__ == "__main__":
    main()
