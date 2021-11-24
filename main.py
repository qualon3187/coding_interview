import json
import sys
from datetime import timedelta
import datetime as datetime



def users():
    u = open('users.json', )
    user = json.load(u)
    u.close()
    return user


def events():
    e = open('events.json', )
    event = json.load(e)
    e.close()
    return event

def scheduleDay(meetingStart,meetingEnd,workDay):
    beginM = meetingStart
    endM = datetime.datetime(2021, 7, 7, 21, 0, 0)
    startD =datetime.datetime(2021, 7, 5, 13, 0, 0) 
    while meetingStart <= meetingEnd:
        if meetingStart in workDay.keys():
            if datetime.datetime.time(meetingStart) == datetime.datetime.time(startD):
                workDay.update({meetingStart:'x'})
            elif  datetime.datetime.time(meetingStart) == datetime.datetime.time(endM):
                workDay.update({meetingStart:'x'})
            elif meetingStart == beginM:
               workDay.update({meetingStart:'s'})
            elif meetingStart == meetingEnd:
                workDay.update({meetingStart:'e'})
            else:
                workDay.update({meetingStart:2})

        meetingStart += timedelta(minutes=15)

    
def calendar(starttime,endtime):
    begin = datetime.datetime.time(starttime)
    end = datetime.datetime.time(endtime)
    week = {}
    while starttime <= endtime:
        time1 = datetime.datetime.time(starttime)
        if begin <= time1 <= end:
            week.update({starttime:'f'})
            
        starttime += timedelta(minutes=15)
                
    return week

    
def main(pers):
    start = datetime.datetime(2021, 7, 5, 13, 0, 0)
    end = datetime.datetime(2021, 7, 7, 21, 0, 0)
    weekdate = datetime.date(2021, 7, 5)
    weekdate2 = datetime.date(2021, 7, 6)
    weekdate3 = datetime.date(2021, 7, 7)
    people = users()
    meeting = events()
    user = pers
    workDay = {}
    begin = start
    endtime = start
    wd = {}
    wd2 = {}
    wd3 = {}
    workList = []

    
    

    for i in user:
        person = i
        for p in people:
            if p["name"] == person:
                personId = p["id"]
                print(p["name"])
                workDay = calendar(start,end)
                
                for d in meeting:
                    if d["user_id"] == personId:
                        d1 = datetime.datetime.strptime(d["start_time"], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.datetime.strptime(d["end_time"], "%Y-%m-%dT%H:%M:%S")
                        date1 = datetime.datetime.date(d1)
                        date2 = datetime.datetime.date(d2)
                        datetime1 = datetime.datetime.time(d1)
                        datetime2 = datetime.datetime.time(d2)
                        scheduleDay(d1,d2,workDay)
                        currentTime = start
                        
                            
                for k,i in workDay.items():
                    currentTime = k
                    if  datetime.datetime(2021, 7, 5, 21, 0) in workDay and workDay[datetime.datetime(2021, 7, 5, 21, 0)] == 'f':
                        workDay.update({ datetime.datetime(2021, 7, 5, 21, 0):'o'})
                    if  datetime.datetime(2021, 7, 6, 21, 0) in workDay and workDay[datetime.datetime(2021, 7, 6, 21, 0)] == 'f':
                        workDay.update({ datetime.datetime(2021, 7, 6, 21, 0):'o'})
                    if  datetime.datetime(2021, 7, 7, 21, 0) in workDay and workDay[datetime.datetime(2021, 7, 7, 21, 0)] == 'f':
                        workDay.update({ datetime.datetime(2021, 7, 7, 21, 0):'o'})
                    if weekdate == datetime.datetime.date(k):
                        if i == 's' or i == 'e' or i == 'f' or i == 'o':
                            wd.update({k:i})
                    if weekdate2 == datetime.datetime.date(k):
                        if i == 's' or i == 'e' or i == 'f' or i == 'o':
                            wd2.update({k:i})
                    if weekdate3 == datetime.datetime.date(k):
                        if i == 's' or i == 'e' or i == 'f' or i == 'o':
                            wd3.update({k:i})
                          

                firstTime = ''
                lastTime =  datetime.datetime(2021, 7, 5, 21, 0)       
                for k,i in wd.items():
                    if firstTime == '':
                        firstTime = k
                    if lastTime < k:
                        ctime = k
                    if i == 's':
                        lastTime = k
                        if lastTime < k:
                            lastTime = cTime
                        print(datetime.datetime.strftime(firstTime, "%Y-%m-%d %H:%M:%S") + '-' + datetime.datetime.strftime(lastTime,"%H:%M:%S"))
                        firstTime = ''
                        
                    if i == 'o':
                        print(datetime.datetime.strftime(firstTime, "%Y-%m-%d %H:%M:%S") + '-' + '21:00:00')

                wd.clear()
                firstTime2 = ''
                lastTime2 =  datetime.datetime(2021, 7, 6, 21, 0)       
                for k,i in wd2.items():
                    if firstTime2 == '':
                        firstTime2 = k
                    if lastTime2 < k:
                        ctime2 = k
                    if i == 's':
                        lastTime2 = k
                        if lastTime2 < k:
                            lastTime2 = cTime2
                        print(datetime.datetime.strftime(firstTime2, "%Y-%m-%d %H:%M:%S") + '-' + datetime.datetime.strftime(lastTime2,"%H:%M:%S"))
                        firstTime2 = ''
                        
                    if i == 'o':
                        print(datetime.datetime.strftime(firstTime2, "%Y-%m-%d %H:%M:%S") + '-' + '21:00:00')

                wd2.clear()
                firstTime3 = ''
                lastTime3 =  datetime.datetime(2021, 7, 7, 21, 0)       
                for k,i in wd3.items():
                    if firstTime3 == '':
                        firstTime3 = k
                    if lastTime3 < k:
                        ctime3 = k
                    if i == 's':
                        lastTime3 = k
                        if lastTime3 < k:
                            lastTime3 = cTime2
                        print(datetime.datetime.strftime(firstTime3, "%Y-%m-%d %H:%M:%S") + '-' + datetime.datetime.strftime(lastTime3,"%H:%M:%S"))
                        firstTime3 = ''
                        
                    if i == 'o':
                        print(datetime.datetime.strftime(firstTime3, "%Y-%m-%d %H:%M:%S") + '-' + '21:00:00')
                    
                wd3.clear()

if __name__ == '__main__':
    main(sys.argv)
    
