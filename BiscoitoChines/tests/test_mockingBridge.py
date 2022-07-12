# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\Note\Desktop\Projeto V&V\project\BiscoitoChines')
import gettingAdvice
from unittest.mock import patch
from unittest import TestCase
import json

# Nestes testes, eu aplico Mock para TDD. Neles, eu defini os comportamentos
# esperados antes de criar as funções em si.

class MockingBridge(TestCase):

    @patch('gettingAdvice.getRandomAdvice')
    
    def test_getting_advice_mocking(self, mock_getRandomAdvice):
        mock_getRandomAdvice.return_value = {"slip": { "id": 16, "advice": "It's unlucky to be superstitious."}}
        bridgeParams = {'params':{'id':'', 'query':''}}
        self.assertEqual(gettingAdvice.bridge(bridgeParams)['slip']['id'], 16)

    @patch('gettingAdvice.getAdviceByID')
    
    def test_getting_advice_by_ID_mocking_valid(self, mock_getAdviceByID):
        mock_getAdviceByID.return_value = {"slip": { "id": 88, "advice": "Hold the door open for the next person."}}
        bridgeParams = {'params':{'id':'88', 'query':''}}
        self.assertEqual(gettingAdvice.bridge(params = bridgeParams)['slip']['advice'], "Hold the door open for the next person.")

    @patch('gettingAdvice.getAdviceByID')

    def test_getting_advice_by_ID_mocking_invalid(self, mock_getAdviceByID):
        mock_getAdviceByID.return_value = "Ei! A gente pediu um número!"
        bridgeParams = {'params':{'id':'letras', 'query':''}}
        self.assertEqual(gettingAdvice.bridge(params = bridgeParams), "Ei! A gente pediu um número!")


    # Esse aqui debaixo é legal, ó! 
    # Eu inda não implementei a função getAdviceByQuery, mas tenho armazenado
    # os resultados que ela deveria ter. Ela, por enquanto, é uma função stub,
    # mas este mock age como se ela estivesse 100% implementada e funcionando
    # direitinho.

    @patch('gettingAdvice.getAdviceByQuery')
    
    def test_getting_advice_by_query_mocking(self, mock_getAdviceByQuery):
        mock_getAdviceByQuery.return_value = {"total_results": "2", "query": "simple", "slips": 
                                                [{"id":82,"advice":"For every complex problem there is an answer that is clear, simple, and wrong.","date":"2016-07-01"},
                                                {"id":138,"advice":"Keep it simple.","date":"2016-02-17"}]}
        bridgeParams = {'params':{'id':'', 'query':'simple'}}
        self.assertEqual(gettingAdvice.bridge(params = bridgeParams)['total_results'], "2")