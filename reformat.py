ticker = "IOTXBTC"
types = ["USD", "USDT", "UST","ETH","BTC"]
tback = ticker[-4:]
currency1 = "null"
for i in types:
    try:
        if i in tback:
            currency1 = i
    except ValueError:
        continue
tfront = ticker[:-len(currency1)]
newticker = tfront + "/" + currency1
print(newticker)
