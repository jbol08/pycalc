"""Utilities related to forex currency converter."""
from forex_python.converter import CurrencyRates, CurrencyCodes

rates = CurrencyRates()
codes = CurrencyCodes()


def check_amount(str):
    try: 
        return float(str)
    except ValueError:
        return None

def check_currency_code(code):
    """check if currency code is in the database"""
    return codes.get_currency_name(code) is not None


def currency_converter(from_currency,to_currency,amount):
   """Convert to a new currency with the correct currency symbol in front"""

   amount = "{:0,.2f}".format(float(rates.convert(from_currency,to_currency,amount)))
    
   symbol = codes.get_symbol(to_currency)
   return f"{symbol}{amount}"