'''
This is a simple currency converter program that converts between euro and dollar based on the current exchange rate.
The program uses the exchangerate-api.com API to fetch the current exchange rate between euro and dollar.

Author: Tim De Paepe & Github Copilot
'''
import requests

def euro_to_dollar(euro):
  """
  Convert euro to dollars based on the current exchange rate.

  Args:
    euro (float): The amount in euro to convert.

  Returns:
    float: The equivalent amount in dollars.
  """
  exchange_rate = fetch_exchange_rate("EUR", "USD")
  return euro * exchange_rate

def dollar_to_euro(dollar):
  """
  Convert dollars to euro based on the current exchange rate.

  Args:
    dollar (float): The amount in dollars to convert.

  Returns:
    float: The equivalent amount in euro.
  """
  exchange_rate = fetch_exchange_rate("USD", "EUR")
  return dollar * exchange_rate


def fetch_exchange_rate(original_currency, target_currency):
  """
  Fetch the current exchange rate from a remote API.

  Args:
    original_currency (str): The original currency to fetch the exchange rate from.
    target_currency (str): The target currency to fetch the exchange rate for.

  Returns:
    float: The exchange rate between the original currency and the target currency.
  """
  url = f"https://api.exchangerate-api.com/v4/latest/{original_currency}"
  response = requests.get(url)
  data = response.json()
  exchange_rate = data["rates"][target_currency]
  return exchange_rate

def delay(seconds):
  """
  Delay the program for a given number of seconds.

  Args:
    seconds (int): The number of seconds to delay.
  """
  import time
  time.sleep(seconds)

def floor(value):
  """
  Floor a float value with 3 decimals.

  Args:
    value (float): The value to floor.

  Returns:
    float: The value floored with 3 decimals.
  """
  return int(value * 1000) / 1000

# Main program
def main():
  print("Welcome to the currency converter!")

  delay(1)

  print("Select the currency to convert to:")
  print("1. EUR --> USD")
  print("2. USD --> EUR")
  selection = input("Enter your choice (1 or 2): ")
  amount = float(input("Enter the amount: "))

  if selection == "1":
    converted_amount = euro_to_dollar(amount)
    converted_amount = floor(converted_amount)
    print(f"{amount} euro is equal to {converted_amount} dollars.")
  elif selection == "2":
    converted_amount = dollar_to_euro(amount)
    converted_amount = floor(converted_amount)
    print(f"{amount} dollar is equal to {converted_amount} euros.")
  else:
    print("Invalid currency selection.")

if __name__ == "__main__":
  main()