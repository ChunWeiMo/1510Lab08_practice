import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import guessing_game


class TestGuessingGame(TestCase):
    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_hit(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        expected_message = 'Nice attack! The foe is killed!\n'
        expected_character = character = {
            'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character, character)

    @patch('builtins.input', side_effect=[3])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_miss(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        expected_message = 'Miss. The foe makes a counterattack. You lose 1 HP.\n'
        expected_character = character = {
            'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 4}
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character, character)


if __name__ == "__main__":
    main()
