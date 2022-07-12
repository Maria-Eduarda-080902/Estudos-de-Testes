# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\Note\Desktop\Projeto V&V\project\BiscoitoChines')
import gettingAdvice
from unittest.mock import patch, Mock
from unittest import TestCase
import json

#Este foi um caso de teste experimental kkkk
# Apenas para ver e demonstrar como o Mock pode substituir e interferir nos
# resultados e retornos de uma função.

class MockingAdvice(TestCase):

    @patch('gettingAdvice.getRandomAdvice') 
    
    def test_getting_advice_mocking(self, mock_getRandomAdvice):
        mock_getRandomAdvice.return_value = {"slip": { "id": 16, "advice": "It's unlucky to be superstitious."}}

        # Você pode retirar os comentários dos prints baixo para conferir 
        # a alteração do método

        #print(mock_getRandomAdvice.return_value)
        #print(gettingAdvice.getRandomAdvice())

        self.assertEqual(gettingAdvice.getRandomAdvice()['slip']['id'], 16)
    
