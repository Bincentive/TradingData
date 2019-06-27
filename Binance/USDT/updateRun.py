import os
import update 
l = []
cwd = os.getcwd()
for i in os.walk(cwd):
    for j in i:
        for k in j:
            if k[0:7] == 'binance':
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
    filename = i
    sss = i.split("-")
    symbol = sss[1]+'/'+sss[2]
    ccc = sss[3].split(".")
    timeframe = ccc[0]
    sec = int(changeTF(ccc[0]))
    print(filename)
    print(symbol)
    if symbol == 'BCHSV/USDT':
        continue
    print(timeframe)
    print(sec)
    print('--------')
    update.update(filename,symbol,timeframe,sec)
    print('done')
    print('--------')
    print('check ok')
    print('--------')
