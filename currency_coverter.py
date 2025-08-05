import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "result" not in data:
        print("Error: Could not fetch conversion rate.")
        return None

    return data["result"]

if __name__ == "__main__":
    print("=== Currency Converter ===")
    from_currency = input("From currency (e.g. USD): ").upper()
    to_currency = input("To currency (e.g. INR): ").upper()
    amount = float(input("Amount to convert: "))

    result = convert_currency(from_currency, to_currency, amount)

    if result is not None:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
