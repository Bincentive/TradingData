import csv
import sys
import datetime
def check(ff):
    haveerro = 0 
    r = csv.reader(open(ff))
    line = [i for i in r]
    now = datetime.datetime.strptime(line[1][0]+line[1][1], "%Y-%m-%d%H:%M:%S")
    j=2
    while(j!=len(line)-1):
        if now < datetime.datetime.strptime(line[j][0]+line[j][1], "%Y-%m-%d%H:%M:%S"):
            now = datetime.datetime.strptime(line[j][0]+line[j][1], "%Y-%m-%d%H:%M:%S")
            j+=1
        else :
            haveerro = 1
            del line[j]
    if haveerro == 1:
        print('have erro')
    writer = csv.writer(open(ff, 'w'))
    writer.writerows(line)

