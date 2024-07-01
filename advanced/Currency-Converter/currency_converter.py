import requests
import json

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"http://data.fixer.io/api/latest?access_key={api_key}"
        self.fx = self.fetch_exchange_rates()

    def fetch_exchange_rates(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        if data.get('success'):
            return data["rates"]
        else:
            raise Exception("Failed to fetch exchange rates")

    def convert(self, amount, from_currency, to_currency):
        from_rate = self.fx.get(from_currency.upper())
        to_rate = self.fx.get(to_currency.upper())
        if from_rate and to_rate:
            amount = float(amount)
            converted_amount = round(amount * to_rate / from_rate, 2)
            return converted_amount
        else:
            raise ValueError("Invalid currency code")
