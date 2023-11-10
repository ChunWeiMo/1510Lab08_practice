from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import 


class Test(TestCase):
    @patch('random.randint', return_value=0)
    def test_(self, _):
        pass
    
    

if __name__ == "__main__":
    main()
