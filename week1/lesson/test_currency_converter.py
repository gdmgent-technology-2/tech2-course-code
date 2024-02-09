import unittest
from unittest.mock import patch
from currency_converter import fetch_exchange_rate

class TestFetchExchangeRate(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_exchange_rate(self, mock_get):
        # Mock the response from the API
        mock_response = {
            "rates": {
                "USD": 1.23,
                "EUR": 0.89,
                "GBP": 0.76
            }
        }
        mock_get.return_value.json.return_value = mock_response

        # Test case 1: Fetching exchange rate from USD to EUR
        exchange_rate = fetch_exchange_rate("USD", "EUR")
        self.assertEqual(exchange_rate, 0.89)

        # Test case 2: Fetching exchange rate from EUR to GBP
        exchange_rate = fetch_exchange_rate("EUR", "GBP")
        self.assertEqual(exchange_rate, 0.76)

        # Test case 3: Fetching exchange rate from GBP to USD
        exchange_rate = fetch_exchange_rate("GBP", "USD")
        self.assertEqual(exchange_rate, 1.23)

if __name__ == '__main__':
    unittest.main()