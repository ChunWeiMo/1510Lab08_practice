from unittest import TestCase
from unittest import main
from simple_game import make_character


class Test(TestCase):
    def test_make_character(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(character, make_character())


if __name__ == "__main__":
    main()
