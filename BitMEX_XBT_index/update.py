# start = csv最後一格的時間轉utc+8 加上 兩個timeframe
import csv
import ccxt
import datetime
import time

def date_plus_times(str1,sec):
    date1 = datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")
    t1 = date1.timetuple()
    timeStamp = int(time.mktime(t1))
    timeStamp+=sec
    date2 = datetime.datetime.fromtimestamp(timeStamp)
    str2 = date2.strftime("%Y-%m-%d %H:%M:%S")
    return str2

def date_forward(str1,sub):
    date1 = datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")
    t1 = date1.timetuple()
    timeStamp = int(time.mktime(t1))
    timeStamp-=sub
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
        sss = list1[ll-1][0]+' '+list1[ll-1][1]
        sss = date_plus_times(sss,28800+int(seconds)*2)
        #c = ccxt.bitmex({'enableRateLimit': True, })
        c = ccxt.bitmex()
        nnn = datetime.datetime.now().timestamp()
        count = 0
        
        while count<=50:
            since = round(time.mktime(datetime.datetime.strptime(sss,"%Y-%m-%d %H:%M:%S").timetuple()))
            if nnn <= since:
                break
            since*=1000

            time.sleep(1)
            
            data = c.fetch_ohlcv(symbol=symbol,timeframe=timeframe, limit=600, since=since, params={})
            for d in data:
                dateArray = datetime.datetime.utcfromtimestamp(d[0]//1000)
                otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                otherStyleTime = date_forward(otherStyleTime,int(seconds))
                da,ti = otherStyleTime.split(" ")
                newdata=[]
                newdata.append(str(da))
                newdata.append(str(ti))
                for i in range(1,5):
                    newdata.append(str(d[i]))
                newdata.append(str(int(round(float(d[5]),0))))
                list1.append(newdata)
            sss = date_plus_times(sss,600*int(seconds))
            
            #print(sss)
            count += 1
            print(count)

    print(filename)
    print(list1[ll-1])
    print(list1[len(list1)-1])

    with open(filename,'w',encoding='utf8',newline='')as csvfile2:
        writer=csv.writer(csvfile2)
        writer.writerows(list1)
