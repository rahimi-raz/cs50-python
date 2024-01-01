import sys
import requests
r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" ).json()

try:
    # if len(sys.argv)>1:
        # if not sys.argv[1].isnumeric():
        #     raise TypeError
        p=float(r['bpi']['USD']['rate_float'])*float(sys.argv[1])
        print(f"${p:,.4f}")
    # else:
    #     raise ValueError
except(ValueError):
    sys.exit("Command-line argument is not a number")
except(IndexError):
    sys.exit("Missing command-line argument")

