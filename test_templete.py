import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from simple_game import 


class Test(TestCase):
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[5])
    def test_(self, _):
        pass
    
    

if __name__ == "__main__":
    main()
