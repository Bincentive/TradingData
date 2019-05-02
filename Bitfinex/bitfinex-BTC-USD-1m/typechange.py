import csv
import ccxt
import datetime
import time
list1=[]
newlist=[]
for yee in range(2013,2019):
    list1=[]
    newlist=[]
    str1=str(yee)+'.csv'
    with open(str1,'r')as csvfile:
        read = csv.reader(csvfile)
        for i in read:
            list1.append(i)
    for i in list1[1:]:
        dateArray = datetime.datetime.utcfromtimestamp(int(i[0])//1000)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        da,ti = otherStyleTime.split(" ")
        newdata=[]
        newdata.append(str(da))
        newdata.append(str(ti))
        for j in range(1,6):
            newdata.append(str(i[j]))
        newlist.append(newdata)
    str2='bit-'+str(yee)+'.csv'
    with open(str2,'w')as csvfile2:
        writer=csv.writer(csvfile2)
        writer.writerows(newlist)