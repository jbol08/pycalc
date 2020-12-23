from unittest import TestCase
from app import app



app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConverterTestCase(TestCase):
    
    def setup(self):
        """setup before each test"""
        self.client = app.test_client()

    def test_converter_form(self):
        with app.test_client() as client:
            
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

    
    def test_redirection_followed(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<label for="convert-to">Convert to:</label>', html)

    def test_currency(self):
        with app.test_client() as client:
            resp = client.get('/result', query_string={
            "convert-from":"USD",
            "convert-to":"USD",
            "amount": 1})

            self.assertEqual(resp.status_code, 200)
            self.assertIn(b'$1.00', resp.data)