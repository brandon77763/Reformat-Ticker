ticker = "IOTXBTC"

types = ["USD", "USDT", "UST","ETH","BTC"]

tback = ticker[-4:]

curency1 = "null"

for i in types:
    try:
        if i in tback:
            curency1 = i
    except ValueError:
        continue

tfront = ticker[:-len(currency1)]

newticker = tfront + "/" + currency1

print(newticket)
