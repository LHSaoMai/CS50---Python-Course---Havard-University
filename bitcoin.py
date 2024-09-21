import json
import requests
import sys

def main():
    user_number = sys.argv
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data_transform = data.json()

    if len(sys.argv) <= 1:
        sys.exit('Missing command-line argument')
    else:
        try:
            x= float(sys.argv[1])
            bitcoin_data = float(data_transform["bpi"]["USD"]["rate_float"])
            buy=x*bitcoin_data
            print(f"${buy:,.4f}")

        except ValueError:
             sys.exit('Command-line argument is not a number')
    #sys.arg

main()
