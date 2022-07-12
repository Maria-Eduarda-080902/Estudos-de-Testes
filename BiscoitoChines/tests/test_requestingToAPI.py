from unittest import TestCase
import requests

# conferindo se a API está funcionando através da URL

class RequestToAPI(TestCase):

    URL = 'https://api.adviceslip.com/advice'

    def test_requesting_random_advice(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)

    def test_requesting_advice_by_id(self):
        newURL = self.URL + "/6"
        response = requests.get(newURL)
        self.assertEqual(response.status_code, 200)

    def test_requesting_advice_by_query(self):
        newURL = self.URL + "/search/simple"
        response = requests.get(newURL)
        self.assertEqual(response.status_code, 200)