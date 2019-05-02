import csv
import ccxt
import datetime
import time
import sys
filename = sys.argv[1]
def date_plus_hours(str1, sec):
    date1 = datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")
    t1 = date1.timetuple()
    timeStamp = int(time.mktime(t1))
    timeStamp+=sec
    date2 = datetime.datetime.fromtimestamp(timeStamp)
    str2 = date2.strftime("%Y-%m-%d %H:%M:%S")
    return str2
def update(filename, symbol, timeframe, seconds):
    list1=[]
    with open(filename,'r')as csvfile:
        read = csv.reader(csvfile)
        for i in read:
            list1.append(i)
        ll=len(list1)
        print(ll)
        sss = int(list1[ll-1][0]) + 60000
        #sss = list1[ll-1][0]+' '+list1[ll-1][1]
        #sss = date_plus_hours(sss,28800+int(seconds))
        c = ccxt.bitfinex()
        nnn = datetime.datetime.now().timestamp()
        while True:
            #since=int(datetime.datetime.strptime(sss, '%Y-%m-%d %H:%M:%S').strftime("%s"))
            if nnn <= sss/1000:
                break
            data = c.fetch_ohlcv(symbol=symbol,timeframe=timeframe, since=sss, limit=600, params={})
            for d in data:
                '''dateArray = datetime.datetime.utcfromtimestamp(d[0]//1000)
                otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                da,ti = otherStyleTime.split(" ")
                newdata=[]
                newdata.append(str(da))
                newdata.append(str(ti))'''
                newdata=[]
                for i in range(0,6):
                    newdata.append(str(d[i]))
                #newdata.append(str(int(round(float(d[5]),0))))
                list1.append(newdata)
            sss = int(data[len(data)-1][0]) + 60000
            with open(filename,'w')as csvfile2:
                writer=csv.writer(csvfile2)
                writer.writerows(list1)
            print(len(list1))
    print(filename)
    print(list1[ll-1])
    print(list1[len(list1)-1])

    with open(filename,'w')as csvfile2:
        writer=csv.writer(csvfile2)
        writer.writerows(list1)
update(filename,'BTCUSD','1m',60)
