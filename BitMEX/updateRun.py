import os
import updateall as b
import fix as f
l = []
cwd = '/Users/roy/workspace/trading-data/TradingData/BitMEX'
for i in os.walk(cwd):
    for j in i:
        for k in j:
            if k[0:6] == 'bitmex':
                l.append(k)
def changeTF(tf):
    if tf == '1m':
        return 60
    if tf == '5m':
        return 5*60
    if tf == '15m':
        return 15*60
    if tf == '30m':
        return 30*60
    if tf == '1h':
        return 60*60
    if tf == '1d':
        return 24*60*60

for i in l:
    filename = '/Users/roy/workspace/trading-data/TradingData/BitMEX/' + i
    sss = i.split("-")
    if 'ETH' == sss[1] or 'BTC' == sss[1]:
        symbol = sss[1]+'/'+sss[2]
        ccc = sss[3].split(".")
        timeframe = ccc[0]
        sec = int(changeTF(ccc[0]))
        print(filename)
        print(symbol)
        print(timeframe)
        print(sec)
        b.update(filename,symbol,timeframe,sec)
        print('done')
        print('--------')
        f.check(filename)
        print('check ok')
        print('--------')
'''    else :
        sss = i.split("-")
        symbol = sss[1]
        ccc = sss[2].split(".")
        timeframe = ccc[0]
        sec = int(changeTF(ccc[0]))
        print(filename)
        print(symbol)
        print(timeframe)
        print(sec)
        b.update(filename,symbol,timeframe,sec)
        print('done')
        print('--------')'''
