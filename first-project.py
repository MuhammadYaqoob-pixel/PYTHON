from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = float(input("Enter amount: "))
from_currency = input("From (e.g. USD): ").upper()
to_currency = input("To (e.g. INR): ").upper()

result = c.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
