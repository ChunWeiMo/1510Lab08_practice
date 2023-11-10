import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_foe(self, mock_output, _):
        check_for_foes()
        expected_message = 'A foe appear! Start a battle!\n'
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(True, check_for_foes())

    @patch('random.randint', return_value=1)
    def test_no_encounter_foe_randint_1(self, _):
        self.assertEqual(False, check_for_foes())

    @patch('random.randint', return_value=2)
    def test_no_encounter_foe_randint_2(self, _):
        self.assertEqual(False, check_for_foes())

    @patch('random.randint', return_value=3)
    def test_no_encounter_foe_randint_3(self, _):
        self.assertEqual(False, check_for_foes())


if __name__ == "__main__":
    main()
