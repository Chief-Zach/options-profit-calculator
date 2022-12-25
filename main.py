import opstrat as op
import nasdaqdatalink


def interest():
    data = nasdaqdatalink.get("USTREASURY/YIELD", rows=1)["10 YR"]
    data = list(data)
    return float(data[0])


def get_price(initial, strike, volitility, days, optionType):
    option = op.black_scholes(
        K=strike,
        St=initial,
        r=interest(),
        t=days,
        v=volitility,
        type=optionType[0].lower()
    )
    print(f"Option Value: {option['value']['option value']}")
    print(f"Intrinsic Value: {option['value']['intrinsic value']}")
    print(f"Time Value (extrinsic): {option['value']['time value']}")
    print(f"Theta: {option['greeks']['theta']}")
    return option
