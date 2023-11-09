import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import room_effect


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_room(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Empty room',
                 (1, 0): 'Camp fire', (1, 0): 'Goal'}
        character = {'X-coordinate': 0,
                     'Y-coordinate': 1, 'Current HP': 5}
        room_effect(board, character)
        game_print = mock_output.getvalue()
        character_expected = {'X-coordinate': 0,
                              'Y-coordinate': 1, 'Current HP': 5}
        expected_output = 'You enter a empty room. Keep going.\n'
        self.assertEqual(expected_output, game_print)
        self.assertEqual(character_expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_spike_trap(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Spike trap',
                 (1, 0): 'Camp fire', (1, 0): 'Goal'}
        character = {'X-coordinate': 0,
                     'Y-coordinate': 1, 'Current HP': 5}
        room_effect(board, character)
        game_print = mock_output.getvalue()
        character_expected = {'X-coordinate': 0,
                              'Y-coordinate': 1, 'Current HP': 4}
        expected_output = 'You get injured by a spike trap, causing 1 damage.\n'
        self.assertEqual(expected_output, game_print)
        self.assertEqual(character_expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_poison_gas(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Poison gas',
                 (1, 0): 'Camp fire', (1, 0): 'Goal'}
        character = {'X-coordinate': 0,
                     'Y-coordinate': 1, 'Current HP': 5}
        room_effect(board, character)
        game_print = mock_output.getvalue()
        character_expected = {'X-coordinate': 0,
                              'Y-coordinate': 1, 'Current HP': 4}
        expected_output = 'You enter a poison chamber. Poison gas has caused 1 damage.\n'
        self.assertEqual(expected_output, game_print)
        self.assertEqual(character_expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_spirit_fountain(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Spirit fountain',
                 (1, 0): 'Camp fire', (1, 0): 'Goal'}
        character = {'X-coordinate': 0,
                     'Y-coordinate': 1, 'Current HP': 5}
        room_effect(board, character)
        game_print = mock_output.getvalue()
        character_expected = {'X-coordinate': 0,
                              'Y-coordinate': 1, 'Current HP': 6}
        expected_output = 'You discover a spirit fountain and get spirit blessing, healing 1 HP.\n'
        self.assertEqual(expected_output, game_print)
        self.assertEqual(character_expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_camp_fire(self, mock_output):
        board = {(0, 0): 'Entrance', (0, 1): 'Camp fire',
                 (1, 0): 'Camp fire', (1, 0): 'Goal'}
        character = {'X-coordinate': 0,
                     'Y-coordinate': 1, 'Current HP': 5}
        room_effect(board, character)
        game_print = mock_output.getvalue()
        character_expected = {'X-coordinate': 0,
                              'Y-coordinate': 1, 'Current HP': 6}
        expected_output = ('You have found a camp fire left by previous adventurers '
                           'and rested for a while, healing 1 HP.\n')
        self.assertEqual(expected_output, game_print)
        self.assertEqual(character_expected, character)


if __name__ == "__main__":
    main()
