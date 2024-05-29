from requests import get
from pprint import PrettyPrinter
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

BASE_URL = "https://api.currencybeacon.com/"
API_KEY = os.getenv("API_KEY")


printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/currencies?api_key={API_KEY}"
    url = BASE_URL + endpoint

    data = get(url).json()['response']
    return data

def print_currencies(currencies):
    for currency in currencies:
        name = currency['name']
        _id = currency['short_code']
        symbol = currency.get("symbol", "")
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2, amount=1):
    endpoint = f"v1/latest?api_key={API_KEY}&base={currency1}&symbols={currency2}"
    url = BASE_URL + endpoint
    data = get(url).json()
    if(len(data['rates']) == 0):
        print("Invalid Currencies")
        return
    
    rate = list(data['rates'].values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    
    return rate


def convert(currency1, currency2, amount):
    #endpoint = f"v1/convert?api_key={API_KEY}&from={currency1}&to={currency2}&amount={amount}"
    rate = exchange_rate("USD", "INR")
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - list the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

if __name__ == "__main__":
    main()