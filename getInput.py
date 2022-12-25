import main
import nasdaqdatalink
import yfinance as yf


def textEntry():
    kind = input("put or call: ")
    initial = input("stock price: ")
    k = input("option strike price: ")
    sigma = input("volitility (%): ")
    r = interest()
    t = input("days remaining: ")
    main.get_price(initial=float(initial), strike=float(k), volitility=float(sigma), interest=float(r), days=int(t),
                   optionType=kind)


# netflix = yf.Ticker("NFLX")
# print(netflix.info)
def interest():
    data = nasdaqdatalink.get("USTREASURY/YIELD", rows=1)["10 YR"]
    data = list(data)
    return float(data[0])


textEntry()
